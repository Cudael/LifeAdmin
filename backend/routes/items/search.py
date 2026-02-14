# backend/routes/items/search.py
from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select, func, or_
from typing import Optional
import logging

from models.item import Item
from models.user import User
from database import get_session
from utils.auth import get_current_user

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/")
def list_items(
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(100, ge=1, le=500, description="Max number of items to return"),
    category: Optional[str] = Query(None, description="Filter by category"),
    item_type: Optional[str] = Query(None, description="Filter by type (document/subscription)"),
    search: Optional[str] = Query(None, description="Search in name and notes"),
    sort_by: Optional[str] = Query("created_at", description="Sort field"),
    sort_order: Optional[str] = Query("desc", pattern="^(asc|desc)$", description="Sort order"),
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    """
    List user's items with pagination, search, and filtering
    """
    # Base query
    query = select(Item).where(Item.user_id == user.id)
    
    # Apply filters
    if category:
        query = query.where(Item.category == category)
    
    if item_type:
        query = query.where(Item.type == item_type)
    
    if search:
        search_term = f"%{search}%"
        query = query.where(
            or_(
                Item.name.ilike(search_term),
                Item.notes.ilike(search_term),
                Item.document_number.ilike(search_term)
            )
        )
    
    # Count total (before pagination)
    count_query = select(func.count()).select_from(query.subquery())
    total = session.exec(count_query).one()
    
    # Apply sorting
    sort_column = getattr(Item, sort_by, Item.created_at)
    if sort_order == "desc":
        query = query.order_by(sort_column.desc())
    else:
        query = query.order_by(sort_column.asc())
    
    # Apply pagination
    query = query.offset(skip).limit(limit)
    
    items = session.exec(query).all()
    
    logger.info(f"📋 Listed {len(items)} items for user {user.email}")
    
    return {
        "items": items,
        "total": total,
        "skip": skip,
        "limit": limit,
        "has_more": (skip + len(items)) < total
    }
