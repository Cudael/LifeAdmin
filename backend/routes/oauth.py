# backend/routes/oauth.py
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlmodel import Session, select
from authlib.integrations.starlette_client import OAuth
import os
from dotenv import load_dotenv
from datetime import datetime

from database import get_session
from models.user import User
from utils.auth import create_access_token

load_dotenv()

router = APIRouter(prefix="/auth", tags=["OAuth"])

# OAuth Configuration
oauth = OAuth()

oauth.register(
    name='google',
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)

@router.get('/google')
async def google_login(request: Request):
    """Initiate Google OAuth flow"""
    redirect_uri = request.url_for('google_callback')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get('/google/callback')
async def google_callback(request: Request, session: Session = Depends(get_session)):
    """Handle Google OAuth callback"""
    try:
        # Get access token from Google
        token = await oauth.google.authorize_access_token(request)
        
        # Get user info from Google
        user_info = token.get('userinfo')
        
        if not user_info:
            raise HTTPException(status_code=400, detail="Failed to get user info from Google")
        
        # Extract user data
        email = user_info.get('email')
        name = user_info.get('name')
        google_id = user_info.get('sub')
        picture = user_info.get('picture')
        email_verified = user_info.get('email_verified', False)  # Google provides this
        
        if not email:
            raise HTTPException(status_code=400, detail="Email not provided by Google")
        
        print(f"Google OAuth: User {email} attempting to sign in")
        
        # Check if user exists
        statement = select(User).where(User.email == email)
        user = session.exec(statement).first()
        
        if not user:
            # Create new user
            print(f"Creating new user: {email}")
            user = User(
                full_name=name or "Google User",
                email=email,
                google_id=google_id,
                profile_picture=picture,
                password_hash=None,  # No password for Google users
                email_verified=True,  # ✅ Google emails are pre-verified
                email_verified_at=datetime.utcnow()  # ✅ Mark when verified
            )
            session.add(user)
            session.commit()
            session.refresh(user)
            print(f"✅ New Google user created and auto-verified: {email}")
        else:
            # Update existing user with Google info
            print(f"User exists: {email}")
            
            # Update Google ID if not set
            if not user.google_id:
                user.google_id = google_id
            
            # Update profile picture if not set
            if not user.profile_picture:
                user.profile_picture = picture
            
            # ✅ Auto-verify email if signing in with Google (even if previously unverified)
            if not user.email_verified and email_verified:
                user.email_verified = True
                user.email_verified_at = datetime.utcnow()
                print(f"✅ Email auto-verified via Google: {email}")
            
            session.add(user)
            session.commit()
        
        # Create JWT token (same format as your login)
        access_token = create_access_token({"sub": str(user.id)})
        
        print(f"Token created for user: {email}")
        
        # Redirect to frontend with token
        frontend_url = os.getenv("FRONTEND_URL", "http://localhost:5173")
        return RedirectResponse(
            url=f"{frontend_url}/auth/callback?token={access_token}"
        )
        
    except Exception as e:
        print(f"OAuth Error: {str(e)}")
        import traceback
        traceback.print_exc()
        
        frontend_url = os.getenv("FRONTEND_URL", "http://localhost:5173")
        return RedirectResponse(
            url=f"{frontend_url}/login?error=oauth_failed"
        )