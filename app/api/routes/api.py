from . import cat
from fastapi import APIRouter


router = APIRouter()
router.include_router(cat.router, tags=["cat"], prefix="/v1")