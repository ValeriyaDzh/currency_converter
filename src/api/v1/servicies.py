import logging

from httpx import AsyncClient, RequestError, HTTPStatusError

from src.schemas.currency import CurrencyFilters
from src.config import settings
from src.utils import valid_currencies
from src.utils.exceptions import DatabaseException, BadRequestException

logger = logging.getLogger(__name__)


class ConverterService:

    async def get_converted_value(self, data: CurrencyFilters):

        if not self._valid_currencies(data.from_, data.to):
            raise BadRequestException("Inccorect currency")

        url = f"{settings.api.URL.get_secret_value()}{data.from_}"
        try:
            async with AsyncClient() as client:
                response = await client.get(url=url, timeout=5)
                if response.status_code == 200:
                    currencies = response.json()["conversion_rates"]
                converted_amount = round(
                    (currencies[data.to] / currencies[data.from_]) * data.value, 2
                )
                return converted_amount

        except RequestError as e:
            logger.error(f"Request error: {e}")
            raise DatabaseException
        except HTTPStatusError as e:
            logger.error(f"HTTP error: {e.response.status_code} - {e.response.text}")
            raise DatabaseException

    @staticmethod
    def _valid_currencies(currency_from: str, currency_to: str) -> bool:
        return currency_from in valid_currencies and currency_to in valid_currencies
