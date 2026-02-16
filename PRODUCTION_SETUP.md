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

    # Frontend
    location / {
        root /var/www/remindes/frontend/dist;
        try_files $uri $uri/ /index.html;
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

    # OAuth callback (direct to backend, not through /api/)
    location /auth/google {
        proxy_pass http://localhost:8000/auth/google;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto https;
        proxy_set_header X-Forwarded-Host $host;
    }
}
```

### 5. Testing OAuth

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

### Common Issues

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
