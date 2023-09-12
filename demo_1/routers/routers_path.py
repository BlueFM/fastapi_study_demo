from . import cat_routers
from fastapi import APIRouter

router = APIRouter()
router.include_router(cat_routers.router, tags=["cat"], prefix="/v1")
