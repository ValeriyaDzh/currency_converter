__all__ = [
    "router_v1",
]

from fastapi import APIRouter

from src.api.v1.routers import router

router_v1 = APIRouter()
router_v1.include_router(router, tags=["Converter | v1"])
