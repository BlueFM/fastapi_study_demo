from . import cat, pine_family
from fastapi import APIRouter


router = APIRouter()
router.include_router(cat.router, tags=["cat"], prefix="/v1")
router.include_router(pine_family.router, tags=["pine_family_members"], prefix="/v1")