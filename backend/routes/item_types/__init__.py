# backend/routes/item_types/__init__.py
from fastapi import APIRouter
from .crud import router as crud_router

router = APIRouter(prefix="/item-types", tags=["item-types"])

router.include_router(crud_router)
