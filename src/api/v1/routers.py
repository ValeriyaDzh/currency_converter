from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, HTTPException, status

from src.api.v1.servicies import ConverterService

from src.schemas import ConvertedValueResponse, CurrencyFilters


router = APIRouter()


@router.get(
    "/rates", status_code=status.HTTP_200_OK, response_model=ConvertedValueResponse
)
async def get_converted_value(
    data: CurrencyFilters = Depends(CurrencyFilters),
    converter_service: ConverterService = Depends(ConverterService),
):
    rate = await converter_service.get_converted_value(data)
    return ConvertedValueResponse(result=rate)
