from fastapi import HTTPException, Depends
from models.user import User
from utils.auth import get_current_user

def require_verified_email(user: User = Depends(get_current_user)) -> User:
    """
    Dependency that requires user to have verified email
    """
    if not user.email_verified:
        raise HTTPException(
            status_code=403,
            detail="Email verification required. Please verify your email to perform this action."
        )
    return user