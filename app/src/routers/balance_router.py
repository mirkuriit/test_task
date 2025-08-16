from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from uuid import UUID

from app.db.connection import get_session

from fastapi import (APIRouter,
                     Depends,
                     Path)

from app.config import config
from app.src.service.balance_service import BalanceService
from app.src.schemas.balance_schema import (BalanceCreate,
                                            BalanceUpdateMax,
                                            BalanceUpdateCurrent,
                                            BalanceGet)


router = APIRouter(
    prefix=f"{config.URL_PREFIX}/balance"
)


@router.post(path='', response_model=BalanceGet)
async def create_balance(
        balance_schema: BalanceCreate,
        session: AsyncSession = Depends(get_session)
):
    balance_service = BalanceService(session)
    balance = await balance_service.create(balance_schema)
    return balance


@router.patch(path='/set/max_balance/{id}', response_model=BalanceGet)
async def set_max_balance(
        transaction_sum: int,
        id_: UUID = Path(..., alias="id"),
        session: AsyncSession = Depends(get_session)
):
    if transaction_sum < 0:
        raise HTTPException(400, detail="negative amount cannot be as max_sum")

    balance_service = BalanceService(session)

    balance = await balance_service.get_by_id(id_=id_)
    current_sum = balance.current_balance
    if transaction_sum < current_sum:
        raise HTTPException(400, detail="incorrect max_balance after transaction")


    balance = await balance_service.update(id_=id_,
                                           balance_upd_schema=BalanceUpdateMax(max_balance=transaction_sum))


    return balance


@router.patch(path='/add/max_balance/{id}', response_model=BalanceGet)
async def add_to_max_balance(
        transaction_sum: int,
        id_: UUID = Path(..., alias="id"),
        session: AsyncSession = Depends(get_session)
):
    if transaction_sum < 0:
        raise HTTPException(400, detail="negative amount cannot be added")

    balance_service = BalanceService(session)

    balance = await balance_service.get_by_id(id_=id_)
    max_sum = balance.max_balance
    balance = await balance_service.update(id_=id_,
                                           balance_upd_schema=BalanceUpdateMax(max_balance=transaction_sum + max_sum))
    return balance


@router.patch(path='/subtract/max_balance/{id}', response_model=BalanceGet)
async def subtract_to_max_balance(
        transaction_sum: int,
        id_: UUID = Path(..., alias="id"),
        session: AsyncSession = Depends(get_session)
):
    if transaction_sum < 0:
        raise HTTPException(400, detail="negative amount cannot be subtracted")

    balance_service = BalanceService(session)
    balance = await balance_service.get_by_id(id_=id_)
    max_sum = balance.max_balance
    current_sum = balance.current_balance

    if max_sum - transaction_sum < 0:
        raise HTTPException(400, detail="max_balance < transaction_sum")
    if (max_sum - transaction_sum) < current_sum:
        raise HTTPException(400, detail="incorrect max_balance after transaction")

    balance = await balance_service.update(id_=id_,
                                           balance_upd_schema=BalanceUpdateMax(max_balance=max_sum - transaction_sum))
    return balance


@router.patch(path='/add/current_balance/{id}', response_model=BalanceGet)
async def add_to_current_balance(
        transaction_sum: int,
        id_: UUID = Path(..., alias="id"),
        session: AsyncSession = Depends(get_session)
):
    if transaction_sum < 0:
        raise HTTPException(400, detail="negative amount cannot be added")

    balance_service = BalanceService(session)

    balance = await balance_service.get_by_id(id_=id_)
    max_sum = balance.max_balance
    current_sum = balance.current_balance

    if transaction_sum + current_sum > max_sum:
        raise HTTPException(400, detail="")

    balance = await balance_service.update(
        id_=id_,
        balance_upd_schema=BalanceUpdateCurrent(current_balance=transaction_sum + current_sum))
    return balance


@router.patch(path='/subtract/current_balance/{id}', response_model=BalanceGet)
async def subtract_to_current_balance(
        transaction_sum: int,
        id_: UUID = Path(..., alias="id"),
        session: AsyncSession = Depends(get_session)
):
    if transaction_sum < 0:
        raise HTTPException(400, detail="negative amount cannot be subtracted")

    balance_service = BalanceService(session)

    balance = await balance_service.get_by_id(id_=id_)
    current_sum = balance.current_balance

    if current_sum - transaction_sum < 0:
        raise HTTPException(400, detail="current_sum < transaction_sum")

    balance = await balance_service.update(
        id_=id_,
        balance_upd_schema=BalanceUpdateCurrent(current_balance=current_sum - transaction_sum))
    return balance


@router.get(path='', response_model=list[BalanceGet])
async def get_balances(
        session: AsyncSession = Depends(get_session)
):
    balance_service = BalanceService(session)
    balances = await balance_service.get_all()
    return balances


@router.get(path='/{id}', response_model=BalanceGet)
async def get_balance(
        id_: UUID = Path(..., alias="id"),
        session: AsyncSession = Depends(get_session)
):
    balance_service = BalanceService(session)
    balance = await balance_service.get_by_id(id_=id_)
    return balance
