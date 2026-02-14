# backend/routes/items/__init__.py
from fastapi import APIRouter

from .crud import router as crud_router
from .search import router as search_router
from .stats import router as stats_router

router = APIRouter(prefix="/items", tags=["Items"])

# Include all sub-routers
router.include_router(stats_router)  # Include stats first to match /stats before /{item_id}
router.include_router(search_router)
router.include_router(crud_router)
