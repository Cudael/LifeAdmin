# Remindes - Complete Setup Guide

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Backend Setup](#backend-setup)
3. [Frontend Setup](#frontend-setup)
4. [Google OAuth Configuration](#google-oauth-configuration)
5. [Running the Project](#running-the-project)
6. [Authentication System Overview](#authentication-system-overview)
7. [Testing the Application](#testing-the-application)
8. [Deployment](#deployment)
9. [Troubleshooting](#troubleshooting)

---

## Prerequisites

- **Python 3.9+** (for backend)
- **Node.js 18+** and npm (for frontend)
- **Git** (for version control)

---

## Backend Setup

### 1. Install Dependencies

```bash
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file in the `backend` directory:

```bash
cd backend
cp .env.example .env
```

Edit `backend/.env` and configure the following:

```env
# ================================
# REQUIRED SETTINGS
# ================================

# Secret key for JWT tokens (REQUIRED - generate a secure random string)
# Generate with: python -c "import secrets; print(secrets.token_urlsafe(32))"
SECRET_KEY=your-generated-secret-key-here

# Frontend URL for CORS (must match exactly, no trailing slash)
FRONTEND_URL=http://localhost:5173

# ================================
# GOOGLE OAUTH (Optional but recommended)
# ================================

# Get from: https://console.cloud.google.com/apis/credentials
GOOGLE_CLIENT_ID=your-google-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-google-client-secret

# OAuth Redirect URI (for production only)
# Leave empty for local development (auto-detects as http://localhost:8000/auth/google/callback)
# For production: https://yourdomain.com/auth/google/callback
OAUTH_REDIRECT_URI=

# ================================
# EMAIL / SMTP (Optional)
# ================================

# For sending verification and notification emails
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password  # Use App Password for Gmail
SMTP_FROM_EMAIL=your-email@gmail.com
SMTP_FROM_NAME=Remindes

# ================================
# STRIPE PAYMENT (Optional)
# ================================

# Get from: https://dashboard.stripe.com/apikeys
STRIPE_SECRET_KEY=sk_test_your_secret_key
STRIPE_PUBLISHABLE_KEY=pk_test_your_publishable_key
STRIPE_PRICE_ID_PREMIUM=price_your_price_id
STRIPE_WEBHOOK_SECRET=whsec_your_webhook_secret

# ================================
# OPTIONAL SETTINGS
# ================================

# Token expiration (uncomment to customize)
# ACCESS_TOKEN_EXPIRE_MINUTES=10080  # 7 days (default)
# REFRESH_TOKEN_EXPIRE_DAYS=30       # 30 days (default)

# Security (production only)
SECURE_COOKIES=false  # Set to 'true' in production with HTTPS
```

**Important Notes:**
- **SECRET_KEY**: Generate with `python -c "import secrets; print(secrets.token_urlsafe(32))"`
- **Gmail SMTP**: Use [App Password](https://support.google.com/accounts/answer/185833), not your regular password
- **Google OAuth**: See detailed setup below

### 3. Initialize Database

```bash
cd backend
python init_db.py
```

This creates a SQLite database (`database.db`) with all required tables:
- `user` - User accounts with OAuth, email verification, and subscriptions
- `item` - Documents and subscriptions
- `item_type` - Templates for item types
- `notification` - Email notifications for expiring items
- `email_verification_tokens` - Email verification tokens
- `password_reset_tokens` - Password reset tokens

### 4. Seed Item Types (Required)

After initializing the database, you must run the migration to seed item types with categories:

```bash
cd backend
python migrations/002_add_dynamic_fields.py
```

This seeds the database with 26 item type templates across 9 categories:
- **Travel**: Passport, Visa
- **Vehicle**: Driver's License, Vehicle Registration, Auto Insurance
- **Personal**: ID Card
- **Health**: Health Insurance Card
- **Legal**: Warranty, Lease Agreement, Property Deed, Legal Contract
- **Financial**: Credit Card, Bank Account, Tax Document
- **Professional**: Professional Certificate, Professional License, Professional Membership
- **Property**: Property-related documents
- **Subscriptions**: Netflix, Spotify, Gym Membership, GitHub, Dropbox, Adobe Creative Cloud, Microsoft 365, Generic Subscription

**Note**: Without this step, the "Add Item" feature will not show any categories!

---

## Frontend Setup

### 1. Install Dependencies

```bash
cd frontend
npm install
```

### 2. Configure Environment Variables

Create a `.env` file in the `frontend` directory:

```bash
cd frontend
cp .env.example .env
```

Edit `frontend/.env`:

```env
# Backend API URL
# Local development:
VITE_API_URL=http://localhost:8000

# Production (with reverse proxy):
# VITE_API_URL=/api

# Production (direct backend URL):
# VITE_API_URL=https://api.yourdomain.com

# Enable Google OAuth (optional)
VITE_ENABLE_GOOGLE_OAUTH=true

# Stripe Publishable Key (optional)
VITE_STRIPE_PUBLISHABLE_KEY=pk_test_your_publishable_key
```

---

## Google OAuth Configuration

### Step 1: Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Navigate to **APIs & Services** → **Credentials**

### Step 2: Create OAuth 2.0 Credentials

1. Click **+ CREATE CREDENTIALS** → **OAuth client ID**
2. If prompted, configure the OAuth consent screen:
   - User Type: **External**
   - App name: **Remindes** (or your app name)
   - User support email: Your email
   - Developer contact: Your email
   - Click **Save and Continue**
   - Scopes: No need to add scopes (default scopes are sufficient)
   - Test users: Add your email for testing
   - Click **Save and Continue**

3. Create OAuth Client ID:
   - Application type: **Web application**
   - Name: **Remindes Web Client**

### Step 3: Configure Redirect URIs

Add the following **Authorized redirect URIs**:

**For Local Development:**
```
http://localhost:8000/auth/google/callback
```

**For Production:**
```
https://yourdomain.com/auth/google/callback
```

### Step 4: Configure Authorized Origins

Add the following **Authorized JavaScript origins**:

**For Local Development:**
```
http://localhost:5173
http://localhost:8000
```

**For Production:**
```
https://yourdomain.com
```

### Step 5: Copy Credentials

1. Copy the **Client ID** and **Client Secret**
2. Add them to `backend/.env`:
   ```env
   GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com
   GOOGLE_CLIENT_SECRET=your-client-secret
   ```

### Step 6: Important Notes

- The redirect URI in Google Console **MUST EXACTLY MATCH** the backend route: `/auth/google/callback`
- For local development, `OAUTH_REDIRECT_URI` can be left empty (auto-detects)
- For production, set `OAUTH_REDIRECT_URI=https://yourdomain.com/auth/google/callback`
- If you change domains, update the redirect URIs in Google Console

---

## Running the Project

### Local Development

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at:
- API: http://localhost:8000
- Docs: http://localhost:8000/docs

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

Frontend will be available at: http://localhost:5173

### Production Build

**Backend:**
```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000
# Or use gunicorn for production:
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

**Frontend:**
```bash
cd frontend
npm run build
# Output will be in: frontend/dist/
```

Serve `frontend/dist/` with a web server (Nginx, Apache, etc.)

---

## Authentication System Overview

### Authentication Methods

Remindes supports two authentication methods:

1. **Email/Password Authentication**
   - User registers with email and password
   - Email verification sent (if SMTP configured)
   - Password must meet strength requirements (8+ chars, uppercase, lowercase, number, special char)
   - Users can reset password via email

2. **Google OAuth**
   - One-click sign-in with Google account
   - No password required
   - Email automatically verified
   - Profile picture imported from Google

### Authentication Flow

#### Email/Password Flow:
1. User registers at `/register` with email and password
2. Backend creates user and sends verification email
3. User receives JWT tokens immediately (can login before verifying)
4. User clicks verification link in email → email marked as verified
5. On subsequent visits, user logs in at `/login`
6. Backend returns access token (7 days) + refresh token (30 days)
7. Frontend stores tokens in localStorage
8. Automatic token refresh runs every hour (refreshes if <1 day remaining)

#### Google OAuth Flow:
1. User clicks "Continue with Google" button
2. Frontend redirects to `{BACKEND_URL}/auth/google`
3. Backend redirects to Google OAuth consent screen
4. User approves and Google redirects to `{BACKEND_URL}/auth/google/callback`
5. Backend:
   - Verifies OAuth token with Google
   - Creates user (if new) or logs in (if exists)
   - Marks email as verified
   - Generates JWT access token + refresh token
   - Redirects to `{FRONTEND_URL}/auth/callback?token={access_token}&refresh_token={refresh_token}`
6. Frontend:
   - Extracts tokens from URL
   - Saves to localStorage
   - Redirects to dashboard
7. Automatic token refresh runs every hour

### JWT Token Details

**Access Token:**
- Lifetime: 7 days (default, configurable)
- Used for authenticating API requests
- Stored in localStorage
- Included in `Authorization: Bearer {token}` header

**Refresh Token:**
- Lifetime: 30 days (default, configurable)
- Used to generate new access tokens
- Stored in localStorage and database (for validation)
- Rotated on each refresh (new refresh token issued)

**Token Refresh:**
- Runs automatically every hour in the background
- Refreshes access token if <1 day remaining
- On refresh failure → user logged out and redirected to login

---

## Testing the Application

### 1. Test Email/Password Registration

1. Navigate to http://localhost:5173
2. Click **Create an account**
3. Fill in the registration form:
   - Full Name: Your Name
   - Email: your-email@example.com
   - Password: Must meet requirements (8+ chars, mixed case, number, special char)
4. Click **Create Account**
5. You should be:
   - Redirected to dashboard
   - Logged in immediately (with or without email verification)
6. Check your email for verification link (if SMTP configured)

### 2. Test Google OAuth

1. Navigate to http://localhost:5173
2. Click **Continue with Google**
3. Select your Google account
4. Approve permissions
5. You should be:
   - Redirected back to the app
   - Logged in with your Google account
   - Profile picture loaded
   - Email marked as verified

### 3. Test Token Refresh

1. Log in with any method
2. Open browser DevTools → Console
3. You should see: `🚀 Starting automatic token refresh check (every hour)`
4. To force a refresh, wait for token to have <1 day remaining, or manually call:
   ```javascript
   import { performTokenRefresh } from './src/utils/tokenRefresh'
   await performTokenRefresh()
   ```
5. Console should show: `✅ Token refreshed successfully`

### 4. Test Protected Routes

1. While logged in, navigate to `/dashboard`, `/items`, `/profile`
2. All should work normally
3. Clear localStorage and refresh
4. You should be redirected to `/login`

### 5. Test Password Reset

1. Navigate to `/login`
2. Click **Forgot password?**
3. Enter your email
4. Check email for reset link (if SMTP configured)
5. Click link and reset password

---

## Deployment

### Environment-Specific Configuration

**Development:**
- Backend: `FRONTEND_URL=http://localhost:5173`
- Frontend: `VITE_API_URL=http://localhost:8000`
- Google OAuth Redirect URI: Auto-detected

**Production:**
- Backend: `FRONTEND_URL=https://yourdomain.com`
- Backend: `OAUTH_REDIRECT_URI=https://yourdomain.com/auth/google/callback`
- Backend: `SECURE_COOKIES=true`
- Frontend: `VITE_API_URL=/api` (if using reverse proxy)
- Update Google Cloud Console redirect URIs

### Recommended Production Setup

Use a reverse proxy (Nginx) to serve both frontend and backend:

```nginx
# Frontend
location / {
    root /var/www/lifeadmin/frontend/dist;
    try_files $uri $uri/ /index.html;
}

# Backend API
location /api/ {
    proxy_pass http://localhost:8000/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}

# Uploads
location /uploads/ {
    proxy_pass http://localhost:8000/uploads/;
}
```

See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed deployment instructions.

---

## Troubleshooting

### OAuth Issues

**Problem:** "Redirect URI mismatch" error
- **Solution:** Make sure the redirect URI in Google Console exactly matches: `http://localhost:8000/auth/google/callback` (dev) or `https://yourdomain.com/auth/google/callback` (prod)

**Problem:** Google login redirects but doesn't log me in
- **Solution:** Check browser console for errors. Ensure `FRONTEND_URL` in backend `.env` matches your frontend URL exactly.

**Problem:** "Invalid credentials" in Google Console
- **Solution:** Ensure `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` in `backend/.env` are correct

### Token Issues

**Problem:** Users getting logged out frequently
- **Solution:** Increase `ACCESS_TOKEN_EXPIRE_MINUTES` in `backend/.env` (default is 7 days)

**Problem:** "Invalid token" errors
- **Solution:** Ensure `SECRET_KEY` is set and consistent across restarts. Never change SECRET_KEY in production or all tokens will be invalidated.

### Email Issues

**Problem:** Verification emails not sending
- **Solution:** 
  - For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833)
  - Check SMTP settings in `backend/.env`
  - Check backend logs for SMTP errors

**Problem:** Emails going to spam
- **Solution:** Configure SPF, DKIM, and DMARC records for your domain

### Database Issues

**Problem:** Database locked errors
- **Solution:** SQLite doesn't handle high concurrency well. For production, consider PostgreSQL:
  ```env
  DATABASE_URL=postgresql://user:password@localhost/lifeadmin
  ```

### CORS Issues

**Problem:** CORS errors in browser console
- **Solution:** Ensure `FRONTEND_URL` in `backend/.env` matches your frontend URL exactly (no trailing slash)

---

## Additional Documentation

- [DEPLOYMENT.md](./DEPLOYMENT.md) - Production deployment guide
- [SECURITY.md](./SECURITY.md) - Security best practices
- [STRIPE_SETUP.md](./STRIPE_SETUP.md) - Stripe payment integration
- [CONFIGURATION.md](./CONFIGURATION.md) - Advanced configuration options

---

## Support

For issues, questions, or contributions, please open an issue on GitHub.
