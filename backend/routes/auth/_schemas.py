"""
Shared Pydantic schemas for authentication routes
"""
from pydantic import BaseModel, EmailStr, validator
from typing import Optional


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr  # ✅ Validates email format
    password: str
    
    @validator('full_name')
    def validate_name(cls, v):
        if not v or len(v.strip()) < 2:
            raise ValueError('Name must be at least 2 characters long')
        if len(v) > 100:
            raise ValueError('Name must not exceed 100 characters')
        return v.strip()
    
    @validator('email')
    def validate_email(cls, v):
        # Check for disposable email domains
        disposable_domains = [
            'tempmail.com', 'throwaway.email', '10minutemail.com',
            'guerrillamail.com', 'mailinator.com', 'trashmail.com'
        ]
        domain = v.split('@')[1].lower()
        if domain in disposable_domains:
            raise ValueError('Disposable email addresses are not allowed')
        return v.lower()


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    token: str
    password: str


class VerifyTokenRequest(BaseModel):
    token: str


class PreferencesUpdate(BaseModel):
    """Validated user display preferences"""
    date_format: Optional[str] = None
    time_format: Optional[str] = None
    items_per_page: Optional[int] = None
    default_sort: Optional[str] = None
    
    @validator('date_format')
    def validate_date_format(cls, v):
        if v is not None:
            allowed_formats = ['MM/DD/YYYY', 'DD/MM/YYYY', 'YYYY-MM-DD', 'DD.MM.YYYY']
            if v not in allowed_formats:
                raise ValueError(f'Invalid date format. Allowed: {", ".join(allowed_formats)}')
        return v
    
    @validator('time_format')
    def validate_time_format(cls, v):
        if v is not None:
            allowed_formats = ['12h', '24h']
            if v not in allowed_formats:
                raise ValueError(f'Invalid time format. Allowed: {", ".join(allowed_formats)}')
        return v
    
    @validator('items_per_page')
    def validate_items_per_page(cls, v):
        if v is not None:
            if v < 5 or v > 100:
                raise ValueError('Items per page must be between 5 and 100')
        return v
    
    @validator('default_sort')
    def validate_default_sort(cls, v):
        if v is not None:
            allowed_sorts = ['expiration_asc', 'expiration_desc', 'title_asc', 'title_desc', 'created_asc', 'created_desc']
            if v not in allowed_sorts:
                raise ValueError(f'Invalid sort option. Allowed: {", ".join(allowed_sorts)}')
        return v


class SettingsUpdate(BaseModel):
    """Validated user account settings"""
    email_notifications_enabled: Optional[bool] = None
    notification_days: Optional[int] = None
    daily_digest: Optional[bool] = None
    language: Optional[str] = None
    timezone: Optional[str] = None
    
    @validator('notification_days')
    def validate_notification_days(cls, v):
        if v is not None:
            if v < 0 or v > 365:
                raise ValueError('Notification days must be between 0 and 365')
        return v
    
    @validator('language')
    def validate_language(cls, v):
        if v is not None:
            # Common language codes
            allowed_languages = ['en', 'es', 'fr', 'de', 'it', 'pt', 'ja', 'zh', 'ko', 'ar', 'ru']
            if v not in allowed_languages:
                raise ValueError(f'Invalid language code. Allowed: {", ".join(allowed_languages)}')
        return v
    
    @validator('timezone')
    def validate_timezone(cls, v):
        if v is not None:
            # Basic validation - accept common patterns
            # For stricter validation, install pytz: pip install pytz
            # and use: pytz.timezone(v) to validate
            if len(v) > 50 or len(v) < 3:
                raise ValueError('Invalid timezone string')
            # Basic format check (e.g., "UTC", "America/New_York")
            if not v.replace('_', '').replace('/', '').replace('-', '').replace('+', '').isalnum():
                raise ValueError('Invalid timezone format')
        return v
