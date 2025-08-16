from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from app.src.schemas.balance_schema import BalanceCreate, BalanceUpdateMax, BalanceUpdateCurrent

from app.db.tables import Balance

from uuid import UUID


class BalanceService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, balance_schema: BalanceCreate):
        balance = Balance(**balance_schema.model_dump())

        self.session.add(balance)
        await self.session.commit()
        await self.session.refresh(balance)

        return balance

    async def get_by_id(self, id_: UUID) -> Balance:
        balance = await self.session.scalar(select(Balance).filter_by(id=id_))
        if balance is None:
            raise HTTPException(404, detail="balance was not found")
        return balance

    async def get_all(self):
        balances = await self.session.scalars(select(Balance))
        return balances

    async def update(self, id_: UUID, balance_upd_schema: BalanceUpdateCurrent | BalanceUpdateMax):
        balance = await self.session.scalar(select(Balance).filter_by(id=id_))
        if balance is None:
            raise HTTPException(404)

        for field, value in balance_upd_schema.model_dump(exclude_none=True).items():
            setattr(balance, field, value)

        await self.session.commit()
        
        return balance
