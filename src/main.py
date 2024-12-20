import logging
import logging.config
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.v1 import router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.config.fileConfig("logging.ini", disable_existing_loggers=False)
    logger = logging.getLogger(__name__)
    logger.info("Starting app...")
    yield


app = FastAPI(title="CurrencyToday", lifespan=lifespan)

app.include_router(router_v1, prefix="/api")
