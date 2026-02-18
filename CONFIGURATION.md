# Configuration Guide for Remindes

This guide explains how to properly configure Remindes after the recent updates that fixed login/registration issues and implemented persistent login.

## Quick Start

### Frontend Configuration

1. **Copy the environment template:**
   ```bash
   cd frontend
   cp .env.example .env
   ```

2. **Edit `.env` and set your backend URL:**
   ```env
   # For local development
   VITE_API_URL=http://localhost:8000
   
   # For production (replace with your actual backend URL)
   # VITE_API_URL=https://api.yourdomain.com
   ```

3. **Build and run:**
   ```bash
   npm install
   npm run dev  # For development
   # OR
   npm run build  # For production
   ```

### Backend Configuration

1. **Copy the environment template:**
   ```bash
   cd backend
   cp .env.example .env
   ```

2. **Edit `.env` and configure required settings:**
   ```env
   # Required: Generate a secure secret key
   SECRET_KEY=your-secret-key-here
   # Generate with: python -c "import secrets; print(secrets.token_urlsafe(32))"
   
   # Required: Set your frontend URL for CORS
   FRONTEND_URL=http://localhost:5173
   
   # Optional: Configure token expiration
   # ACCESS_TOKEN_EXPIRE_MINUTES=30   # 30 minutes (recommended for security)
   # REFRESH_TOKEN_EXPIRE_DAYS=30     # 30 days (default)
   ```

3. **Run the backend:**
   ```bash
   pip install -r requirements.txt
   python migrate.py
   uvicorn main:app --reload
   ```

## What Was Fixed

### 1. Login and Registration URL Issues

**Problem:** The frontend had hardcoded `http://localhost:8000` URLs, causing login redirects and API calls to fail when deployed.

**Solution:** All URLs now use the `VITE_API_URL` environment variable, making the application deployment-ready.

**Affected Files:**
- Login Google OAuth redirect
- API calls for login/registration
- File upload/download links
- Document preview links

### 2. Users Being Logged Out

**Problem:** Users were automatically logged out after 30 minutes due to short access token expiration.

**Solution:** Implemented a comprehensive persistent login system:

- **Longer Token Lifetime:** Access tokens now last 7 days by default (configurable)
- **Automatic Token Refresh:** Background process checks token expiration every hour
- **Smart Refresh Logic:** Tokens are refreshed when less than 1 day remains
- **Seamless Experience:** Users stay logged in indefinitely without interruption

## Token Configuration

### Understanding Token Expiration

Remindes uses two types of tokens:

1. **Access Token:** Used for API authentication. Default: 30 minutes (recommended for security)
2. **Refresh Token:** Used to generate new access tokens. Default: 30 days

### Customizing Token Expiration

Edit your backend `.env` file:

```env
# Default (recommended for security)
ACCESS_TOKEN_EXPIRE_MINUTES=30  # 30 minutes

# Allow refresh tokens to work for 30 days
REFRESH_TOKEN_EXPIRE_DAYS=30
```

**Important Notes:**
- Access token expiration should be less than refresh token expiration
- The frontend automatically refreshes tokens when less than 1 day remains
- Longer tokens = better UX but slightly less secure if a token is stolen
- For high-security applications, consider shorter expiration times

### Security Considerations

**Default Settings (Recommended for most users):**
- Access Token: 7 days - Good balance between UX and security
- Refresh Token: 30 days - Users re-login monthly

**High Security (Banks, Healthcare):**
```env
ACCESS_TOKEN_EXPIRE_MINUTES=60      # 1 hour
REFRESH_TOKEN_EXPIRE_DAYS=1         # 1 day
```

**Maximum Convenience (Personal use):**
```env
ACCESS_TOKEN_EXPIRE_MINUTES=525600  # 1 year
REFRESH_TOKEN_EXPIRE_DAYS=365       # 1 year
```

## Deployment Checklist

### Frontend Deployment

- [ ] Set `VITE_API_URL` to your production backend URL
- [ ] Run `npm run build`
- [ ] Deploy the `dist` folder to your hosting service
- [ ] Ensure your hosting service serves `index.html` for all routes (SPA mode)

### Backend Deployment

- [ ] Generate a secure `SECRET_KEY` (min 32 characters)
- [ ] Set `FRONTEND_URL` to your production frontend URL
- [ ] Configure token expiration times if needed
- [ ] Set `SECURE_COOKIES=true` if using HTTPS
- [ ] Run database migrations
- [ ] Start the backend server

### Environment-Specific URLs

**Development:**
```env
# Frontend .env
VITE_API_URL=http://localhost:8000

# Backend .env
FRONTEND_URL=http://localhost:5173
```

**Production:**
```env
# Frontend .env
VITE_API_URL=https://api.yourdomain.com

# Backend .env
FRONTEND_URL=https://yourdomain.com
```

## Troubleshooting

### Login Redirect Issues

**Symptom:** After logging in, you're redirected to localhost:8000

**Solution:**
1. Check that `VITE_API_URL` is set correctly in frontend `.env`
2. Rebuild the frontend: `npm run build`
3. Clear your browser cache
4. Try logging in again

### Registration Fails with "Failed to fetch"

**Symptom:** Registration form shows "TypeError: Failed to fetch"

**Solution:**
1. Verify `VITE_API_URL` matches your backend URL
2. Ensure backend is running and accessible
3. Check browser console for CORS errors
4. Verify backend `FRONTEND_URL` includes your frontend URL

### Users Still Being Logged Out

**Symptom:** Users are logged out after some time

**Possible Causes:**
1. Token expiration is too short - increase `ACCESS_TOKEN_EXPIRE_MINUTES`
2. Browser is clearing localStorage - check browser privacy settings
3. Backend secret key changed - users must re-login after key changes

### File Links Not Working

**Symptom:** Document previews/downloads show 404 errors

**Solution:**
1. Verify `VITE_API_URL` is set correctly
2. Check that backend uploads directory is accessible
3. Ensure file paths in database are correct

## Additional Resources

- [Vite Environment Variables](https://vitejs.dev/guide/env-and-mode.html)
- [FastAPI Configuration](https://fastapi.tiangolo.com/advanced/settings/)
- [JWT Best Practices](https://tools.ietf.org/html/rfc8725)

## Support

If you encounter issues not covered in this guide:
1. Check the main README.md
2. Review the Security section in README.md
3. Open a GitHub issue with:
   - Your environment (development/production)
   - Steps to reproduce
   - Error messages from browser console and backend logs
