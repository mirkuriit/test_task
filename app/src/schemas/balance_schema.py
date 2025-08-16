from typing import Any

from pydantic import BaseModel, ConfigDict, field_validator, model_validator
import uuid

from typing_extensions import Self


class BaseBalance(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class BalanceCreate(BaseBalance):
    max_balance: int
    current_balance: int

    @field_validator('max_balance')
    def is_max_balance_correct(cls, value):
        if value < 0:
            raise ValueError("max_balance must be > 0")
        return value

    @field_validator('current_balance')
    def is_current_balance_correct(cls, value):
        if value < 0:
            raise ValueError("current_balance must be > 0")
        return value

    @model_validator(mode='after')
    def is_current_balance_correct(self):
        if self.current_balance >= self.max_balance:
            raise ValueError('current_balance must be < max_balance')
        return self

class BalanceUpdateCurrent(BaseBalance):
    current_balance: int


class BalanceUpdateMax(BaseBalance):
    max_balance: int


class BalanceGet(BaseBalance):
    id: uuid.UUID
    user_id: uuid.UUID
    max_balance: int
    current_balance: int