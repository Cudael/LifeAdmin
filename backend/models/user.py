from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    full_name: str
    email: str
    password_hash: str

    # Access token (optional — you can remove this later)
    token: Optional[str] = None

    # NEW: Refresh token + expiration
    refresh_token: Optional[str] = None
    refresh_token_expires: Optional[datetime] = None