# models/item.py
from sqlmodel import SQLModel, Field
from datetime import date, datetime
from typing import Optional
import json

class ItemBase(SQLModel):
    # Shared fields
    name: str
    category: str
    type: str  # "document" or "subscription"
    
    # Item type reference (optional - links to ItemType for dynamic fields)
    item_type_id: Optional[int] = None
    item_type_name: Optional[str] = None  # Denormalized for display

    # Legacy document fields (kept for backward compatibility)
    expiration_date: Optional[date] = None
    document_number: Optional[str] = None

    # Legacy subscription fields (kept for backward compatibility)
    renewal_date: Optional[date] = None
    billing_cycle: Optional[str] = None
    price: Optional[float] = None

    # Shared optional fields
    file_path: Optional[str] = None
    notes: Optional[str] = None
    
    # Custom reminder schedule (optional - falls back to user's default if not set)
    reminder_days_before: Optional[int] = None
    
    # Dynamic fields stored as JSON (new approach)
    dynamic_fields: Optional[str] = Field(default="{}")  # JSON string


class Item(ItemBase, table=True):
    __tablename__ = "items"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    
    # Timestamps
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    
    # Helper method to get dynamic fields as dict
    def get_dynamic_fields(self) -> dict:
        """Parse and return dynamic fields"""
        try:
            return json.loads(self.dynamic_fields or "{}")
        except:
            return {}
    
    def set_dynamic_fields(self, fields: dict):
        """Set dynamic fields from dict"""
        self.dynamic_fields = json.dumps(fields)
    
    # Helper method to get the relevant expiry date
    def get_expiry_date(self) -> Optional[date]:
        """Returns the appropriate expiry date based on item type"""
        # First check dynamic fields
        dyn_fields = self.get_dynamic_fields()
        if "expiration_date" in dyn_fields:
            try:
                return date.fromisoformat(dyn_fields["expiration_date"])
            except:
                pass
        if "renewal_date" in dyn_fields:
            try:
                return date.fromisoformat(dyn_fields["renewal_date"])
            except:
                pass
        
        # Fall back to legacy fields
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
    
    # Item type reference
    item_type_id: Optional[int] = None
    item_type_name: Optional[str] = None

    # Legacy document fields
    expiration_date: Optional[date] = None
    document_number: Optional[str] = None

    # Legacy subscription fields
    renewal_date: Optional[date] = None
    billing_cycle: Optional[str] = None
    price: Optional[float] = None

    # Shared
    file_path: Optional[str] = None
    notes: Optional[str] = None
    
    # Custom reminder schedule
    reminder_days_before: Optional[int] = None
    
    # Dynamic fields
    dynamic_fields: Optional[str] = None