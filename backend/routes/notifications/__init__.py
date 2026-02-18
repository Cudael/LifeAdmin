# routes/notifications/__init__.py
from fastapi import APIRouter
from .list import router as list_router
from .crud import router as crud_router

router = APIRouter(tags=["Notifications"])

router.include_router(list_router)
router.include_router(crud_router)
