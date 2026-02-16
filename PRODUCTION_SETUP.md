# Production Deployment Guide

## Google OAuth Configuration

### 1. Google Cloud Console Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/apis/credentials)
2. Select your OAuth 2.0 Client ID (or create a new Web application client)
3. Configure **Authorized JavaScript origins**:
   - `https://remindes.com`
   - `https://www.remindes.com`
   - `http://localhost:5173` (for local testing)

4. Configure **Authorized redirect URIs**:
   - `https://remindes.com/auth/google/callback`
   - `https://www.remindes.com/auth/google/callback`
   - `http://localhost:8000/auth/google/callback` (for local testing)

5. Save your changes

### 2. Backend Configuration

Create `backend/.env` with production values:

```bash
# Required
SECRET_KEY=your-production-secret-key
FRONTEND_URL=https://remindes.com

# Google OAuth
GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-client-secret

# CRITICAL: Set this to match your Google Console redirect URI
OAUTH_REDIRECT_URI=https://remindes.com/auth/google/callback

# Production security
SECURE_COOKIES=true
```

### 3. Frontend Configuration

Create `frontend/.env`:

```bash
# For production with reverse proxy (Nginx)
VITE_API_URL=/api

# Enable OAuth
VITE_ENABLE_GOOGLE_OAUTH=true
```

### 4. Nginx Configuration Example

If using Nginx as a reverse proxy:

```nginx
server {
    listen 443 ssl http2;
    server_name remindes.com www.remindes.com;

    # SSL configuration
    ssl_certificate /path/to/ssl/cert.pem;
    ssl_certificate_key /path/to/ssl/key.pem;

    # ⚠️ CRITICAL: OAuth routes MUST be defined BEFORE the frontend location block!
    # This ensures /auth/google and /auth/google/callback are proxied to backend
    # instead of being served by the frontend router
    location /auth/ {
        proxy_pass http://localhost:8000/auth/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Host $host;
        proxy_redirect off;
    }

    # Backend API
    location /api/ {
        proxy_pass http://localhost:8000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Host $host;
        proxy_redirect off;
    }

    # Frontend - MUST come AFTER API and auth routes!
    # The try_files directive serves the Vue.js SPA
    location / {
        root /var/www/remindes/frontend/dist;
        try_files $uri $uri/ /index.html;
    }
}
```

### 5. Understanding the Nginx Configuration

**Why Order Matters:**

Nginx processes location blocks in a specific order. When a request comes in, Nginx checks location blocks to find the best match. The `location /` block is a catch-all that matches everything, so if it comes first, it will serve the frontend for ALL requests including `/auth/google/callback`.

**Correct Order:**
1. ✅ `location /auth/` - Most specific, handles OAuth routes
2. ✅ `location /api/` - Specific, handles API routes  
3. ✅ `location /` - Least specific, serves frontend as fallback

**What Happens if Order is Wrong:**
```nginx
# ❌ WRONG - Frontend will handle /auth/google/callback
location / { ... }           # Matches everything first!
location /auth/ { ... }      # Never reached for /auth/* paths
```

When the order is wrong:
1. User clicks "Sign in with Google"
2. Backend redirects to Google
3. Google redirects to `https://remindes.com/auth/google/callback?code=...&state=...`
4. Nginx serves `index.html` (frontend) instead of proxying to backend
5. Vue Router's catch-all route redirects user to landing page
6. OAuth parameters are visible in URL but login fails

**Testing Your Configuration:**

Use the provided helper script to verify your Nginx configuration:

```bash
# Make the script executable
chmod +x nginx-check.sh

# Run the verification script
./nginx-check.sh
```

The script will:
- ✅ Check if Nginx is installed
- ✅ Find your Nginx configuration file
- ✅ Verify `/auth/` proxy configuration exists
- ✅ Check location block order is correct
- ✅ Test Nginx configuration syntax
- ✅ Provide helpful error messages and suggestions

If all checks pass, apply the configuration:

```bash
# Test configuration syntax
sudo nginx -t

# If test passes, reload Nginx
sudo systemctl reload nginx

# Or restart if reload doesn't work
sudo systemctl restart nginx
```

### 6. Testing OAuth

After deployment:

1. Check backend logs for the redirect URI being used:
   ```bash
   # Look for this line in logs:
   🔐 Google OAuth initiated with redirect URI: https://remindes.com/auth/google/callback
   ```

2. Verify it matches your Google Console configuration exactly

3. Test the OAuth flow:
   - Click "Sign in with Google"
   - Should redirect to Google consent screen
   - After consent, should redirect back to your app

### 7. Common Issues

**Understanding the OAuth Flow:**

When OAuth is working correctly:
1. User clicks "Sign in with Google" on frontend
2. Frontend sends request to `/api/auth/google` (proxied to backend)
3. Backend redirects user to Google consent screen
4. User approves on Google
5. Google redirects to `https://remindes.com/auth/google/callback?code=...&state=...`
6. ✅ **Nginx proxies this to backend** (NOT frontend)
7. Backend exchanges code for user info, creates JWT token
8. Backend redirects to `https://remindes.com/auth/callback?token=...`
9. Frontend handles this route, saves token, redirects to dashboard

If `/auth/google/callback` goes to frontend instead of backend, the flow breaks at step 6.

**401: invalid_client**
- Redirect URI mismatch between your app and Google Console
- Check the `OAUTH_REDIRECT_URI` in backend `.env`
- Verify it's listed in Google Console's "Authorized redirect URIs"

**CORS errors**
- Check `FRONTEND_URL` in backend `.env` matches your domain
- Verify Nginx proxy headers are set correctly

**Redirect loops**
- Check that frontend `VITE_API_URL` is correct
- Verify Nginx configuration for `/auth/google` path

**OAuth callback goes to frontend (landing page with query params in URL)**
- This is the main issue this guide addresses
- Check Nginx configuration has `location /auth/` BEFORE `location /`
- Run `./nginx-check.sh` to verify configuration
- Check backend logs - if you don't see "OAuth callback" logs, the request isn't reaching the backend

**How to verify requests are reaching backend:**

Monitor backend logs while testing OAuth:
```bash
# In backend directory, watch logs
tail -f app.log

# Or if running with uvicorn
# Watch the console output
```

You should see:
```
🔐 Google OAuth initiated with redirect URI: https://remindes.com/auth/google/callback
Google OAuth: User email@example.com attempting to sign in
OAuth token created for user: email@example.com
```

If you don't see these logs when clicking "Sign in with Google" or after Google redirects, then:
- For the first log: Your `/api/auth/google` request isn't reaching the backend
- For callback logs: Your `/auth/google/callback` request is going to frontend instead of backend
