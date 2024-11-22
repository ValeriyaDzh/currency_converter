from dataclasses import dataclass

from fastapi import Query
from pydantic import BaseModel


@dataclass
class CurrencyFilters:
    from_: str = Query(..., alias="from")
    to: str = Query(...)
    value: int = Query(...)


class ConvertedValueResponse(BaseModel):
    result: float
