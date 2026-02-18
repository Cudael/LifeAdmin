# backend/routes/items/stats.py
from fastapi import APIRouter, Depends
from sqlmodel import Session, select, func
from datetime import datetime, timedelta, date
from calendar import monthrange
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
    
    now = datetime.utcnow()
    today = date.today()
    
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
    thirty_days_future = today + timedelta(days=30)
    
    expiring_soon = session.exec(
        select(func.count(Item.id))
        .where(Item.user_id == user.id)
        .where(Item.expiration_date.isnot(None))
        .where(Item.expiration_date <= thirty_days_future)
        .where(Item.expiration_date >= today)
    ).one()
    
    # Expiring this week (next 7 days)
    seven_days_future = today + timedelta(days=7)
    
    expiring_this_week = session.exec(
        select(func.count(Item.id))
        .where(Item.user_id == user.id)
        .where(Item.expiration_date.isnot(None))
        .where(Item.expiration_date <= seven_days_future)
        .where(Item.expiration_date >= today)
    ).one()
    
    # Expired items
    expired_items = session.exec(
        select(func.count(Item.id))
        .where(Item.user_id == user.id)
        .where(Item.expiration_date.isnot(None))
        .where(Item.expiration_date < today)
    ).one()
    
    # Documents total
    documents_total = session.exec(
        select(func.count(Item.id))
        .where(Item.user_id == user.id)
        .where(Item.type == "document")
    ).one()
    
    # Subscriptions total
    subscriptions_total = session.exec(
        select(func.count(Item.id))
        .where(Item.user_id == user.id)
        .where(Item.type == "subscription")
    ).one()
    
    # Subscriptions renewing in next 7 days
    subscriptions_renewing_week = session.exec(
        select(func.count(Item.id))
        .where(Item.user_id == user.id)
        .where(Item.type == "subscription")
        .where(Item.renewal_date.isnot(None))
        .where(Item.renewal_date <= seven_days_future)
        .where(Item.renewal_date >= today)
    ).one()
    
    # Items added this month (last 30 days)
    thirty_days_past = now - timedelta(days=30)
    
    items_added_this_month = session.exec(
        select(func.count(Item.id))
        .where(Item.user_id == user.id)
        .where(Item.created_at >= thirty_days_past)
    ).one()
    
    # Items expiring this month (current calendar month)
    year = today.year
    month = today.month
    _, last_day = monthrange(year, month)
    month_start = date(year, month, 1)
    month_end = date(year, month, last_day)
    
    items_expiring_this_month = session.exec(
        select(func.count(Item.id))
        .where(Item.user_id == user.id)
        .where(Item.expiration_date.isnot(None))
        .where(Item.expiration_date >= month_start)
        .where(Item.expiration_date <= month_end)
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
        "expiring_this_week": expiring_this_week,
        "expired": expired_items,
        "documents": documents_total,
        "subscriptions": subscriptions_total,
        "by_category": {cat: count for cat, count in categories},
        "activity_summaries": {
            "items_added_this_month": items_added_this_month,
            "items_expiring_this_month": items_expiring_this_month,
            "items_expiring_this_week": expiring_this_week,
            "expired_items": expired_items,
            "subscriptions_renewing_week": subscriptions_renewing_week,
            "documents_total": documents_total
        }
    }
