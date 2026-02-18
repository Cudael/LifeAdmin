# backend/routes/items/stats.py
from fastapi import APIRouter, Depends
from sqlmodel import Session, select, func
from datetime import datetime, timedelta
import logging

from models.item import Item
from models.user import User
from database import get_session
from utils.auth import get_current_user

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/items/stats")
@router.get("/items/stats/")
def get_item_stats(
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    """Get user's item statistics"""
    
    # Total items
    total_items = session.exec(
        select(func.count(Item.id)).where(Item.user_id == user.id)
    ).one()
    
    # Active subscriptions
    active_subscriptions = session.exec(
        select(func.count(Item.id))
        .where(Item.user_id == user.id)
        .where(Item.type == "subscription")
        .where(
            (Item.billing_cycle.isnot(None)) | 
            (Item.renewal_date.isnot(None))
        )
    ).one()
    
    # Expiring soon (next 30 days)
    thirty_days = datetime.utcnow() + timedelta(days=30)
    
    expiring_soon = session.exec(
        select(func.count(Item.id))
        .where(Item.user_id == user.id)
        .where(Item.expiration_date.isnot(None))
        .where(Item.expiration_date <= thirty_days)
        .where(Item.expiration_date >= datetime.utcnow())
    ).one()
    
    # Count by category
    categories = session.exec(
        select(Item.category, func.count(Item.id))
        .where(Item.user_id == user.id)
        .group_by(Item.category)
    ).all()
    
    return {
        "total_items": total_items,
        "active_subscriptions": active_subscriptions,
        "expiring_soon": expiring_soon,
        "by_category": {cat: count for cat, count in categories}
    }
