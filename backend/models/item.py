# models/item.py
from sqlmodel import SQLModel, Field
from datetime import date, datetime
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
    
    # Custom reminder schedule (optional - falls back to user's default if not set)
    reminder_days_before: Optional[int] = None


class Item(ItemBase, table=True):
    __tablename__ = "items"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    
    # Timestamps
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    
    # Helper method to get the relevant expiry date
    def get_expiry_date(self) -> Optional[date]:
        """Returns the appropriate expiry date based on item type"""
        if self.type == "document":
            return self.expiration_date
        elif self.type == "subscription":
            return self.renewal_date
        return None
    
    # Helper method to check if item is expiring soon
    def is_expiring_soon(self, days: int = 7) -> bool:
        """Check if item expires within the given number of days"""
        expiry = self.get_expiry_date()
        if not expiry:
            return False
        
        days_until = (expiry - date.today()).days
        return 0 <= days_until <= days
    
    # Helper method to check if expired
    def is_expired(self) -> bool:
        """Check if item has expired"""
        expiry = self.get_expiry_date()
        if not expiry:
            return False
        
        return expiry < date.today()


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
    
    # Custom reminder schedule
    reminder_days_before: Optional[int] = None