from sqlmodel import SQLModel, Field
from datetime import date
from typing import Optional

class ItemBase(SQLModel):
    # Shared fields
    name: str
    category: str
    type: str  # "document" or "subscription"

    # Document fields
    expiration_date: Optional[date] = None
    document_number: Optional[str] = None

    # Subscription fields
    renewal_date: Optional[date] = None
    billing_cycle: Optional[str] = None
    price: Optional[float] = None

    # Shared optional fields
    file_path: Optional[str] = None
    notes: Optional[str] = None


class Item(ItemBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")


class ItemCreate(ItemBase):
    pass


class ItemUpdate(SQLModel):
    name: Optional[str] = None
    category: Optional[str] = None
    type: Optional[str] = None

    # Document
    expiration_date: Optional[date] = None
    document_number: Optional[str] = None

    # Subscription
    renewal_date: Optional[date] = None
    billing_cycle: Optional[str] = None
    price: Optional[float] = None

    # Shared
    file_path: Optional[str] = None
    notes: Optional[str] = None