# LifeAdmin Setup Guide

## Prerequisites
- Python 3.9+
- Node.js 18+
- SQLite (included with Python)

## Backend Setup

### 1. Install Dependencies

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Environment Variables

Create `backend/.env`:

```env
# Security
SECRET_KEY=your-secret-key-here-generate-with-openssl-rand-hex-32

# Google OAuth
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
OAUTH_REDIRECT_URI=https://yourdomain.com/auth/google/callback

# Frontend
FRONTEND_URL=https://yourdomain.com

# Email (optional - for verification emails)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password

# Stripe (optional - for subscriptions)
STRIPE_SECRET_KEY=your-stripe-secret-key
STRIPE_PUBLISHABLE_KEY=your-stripe-publishable-key
STRIPE_WEBHOOK_SECRET=your-stripe-webhook-secret

# Security (production only)
SECURE_COOKIES=false  # Set to 'true' in production with HTTPS
```

**Important Notes:**
- Generate a secure SECRET_KEY: `openssl rand -hex 32`
- For Google OAuth, create credentials at: https://console.cloud.google.com/apis/credentials
- For Gmail SMTP, use an App Password (not your regular password): https://support.google.com/accounts/answer/185833

### 3. Initialize Database

```bash
cd backend
python init_db.py
```

This will:
- Delete any existing `database.db` (after confirmation)
- Create a fresh database with all required tables:
  - **user** - User accounts with OAuth, email verification, preferences, and subscription fields
  - **items** - Documents and subscriptions with dynamic fields
  - **item_types** - Templates for different item types
  - **notifications** - User notifications for expiring items

### 4. Run Backend

```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: `http://localhost:8000`

API documentation: `http://localhost:8000/docs`

## Frontend Setup

### 1. Install Dependencies

```bash
cd frontend
npm install
```

### 2. Environment Variables

Create `frontend/.env`:

```env
VITE_API_URL=http://localhost:8000
```

For production:
```env
VITE_API_URL=https://yourdomain.com/api
```

### 3. Build & Run

**Development:**
```bash
npm run dev
```

The frontend will be available at: `http://localhost:5173`

**Production build:**
```bash
npm run build
```

Build output will be in `frontend/dist/`

## Production Deployment

### Nginx Configuration

Add OAuth routing to your nginx config. **Important:** The `/auth/` location block must come **before** the frontend `/` location block:

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    # OAuth routes - MUST come before frontend location /
    location /auth/ {
        proxy_pass http://localhost:8000/auth/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Backend API
    location /api/ {
        proxy_pass http://localhost:8000/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Uploaded files
    location /uploads/ {
        proxy_pass http://localhost:8000/uploads/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    # Frontend - MUST come after /auth/ and /api/ locations
    location / {
        root /home/lifeadmin/LifeAdmin/frontend/dist;
        try_files $uri $uri/ /index.html;
    }
}
```

**For HTTPS (recommended):**
- Use certbot to get free SSL certificates: `sudo certbot --nginx -d yourdomain.com`
- Update `backend/.env`: Set `SECURE_COOKIES=true`

### Systemd Service

Create `/etc/systemd/system/lifeadmin-backend.service`:

```ini
[Unit]
Description=LifeAdmin Backend API
After=network.target

[Service]
Type=simple
User=lifeadmin
WorkingDirectory=/home/lifeadmin/LifeAdmin/backend
Environment="PATH=/home/lifeadmin/LifeAdmin/backend/venv/bin"
ExecStart=/home/lifeadmin/LifeAdmin/backend/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable lifeadmin-backend
sudo systemctl start lifeadmin-backend
sudo systemctl status lifeadmin-backend
```

View logs:
```bash
sudo journalctl -u lifeadmin-backend -f
```

## Testing Authentication

### Test Regular Registration

1. Navigate to `http://localhost:5173/register` (or your domain)
2. Fill in:
   - Full Name
   - Email address
   - Password
3. Click "Register"
4. Check your email for the verification link
5. Click the verification link to verify your email
6. Navigate to `/login` and sign in with your credentials

### Test Google OAuth

1. Navigate to `http://localhost:5173/login` (or your domain)
2. Click "Sign in with Google"
3. Select your Google account or sign in
4. Authorize the application
5. You should be redirected to the dashboard, automatically signed in
6. Your email is automatically verified (no verification email needed)

**Note:** Google OAuth requires:
- Valid `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` in backend `.env`
- `OAUTH_REDIRECT_URI` must match the redirect URI configured in Google Console
- The redirect URI in Google Console should be: `https://yourdomain.com/auth/google/callback`

### Test Login After Registration

1. Navigate to `/login`
2. Enter your email and password
3. Click "Login"
4. If email is verified, you'll be redirected to the dashboard
5. If email is not verified, you'll see an error message

## Troubleshooting

### OAuth not working

**Symptoms:** Clicking "Sign in with Google" doesn't redirect or shows errors

**Solutions:**
1. Check `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` are set correctly in `backend/.env`
2. Verify `OAUTH_REDIRECT_URI` in `.env` matches Google Console:
   ```bash
   # In Google Console, authorized redirect URIs should include:
   https://yourdomain.com/auth/google/callback
   ```
3. Ensure nginx has the `/auth/` location block configured
4. Check backend logs:
   ```bash
   sudo journalctl -u lifeadmin-backend -f
   ```
5. Verify the frontend `VITE_API_URL` is correct

### Database errors

**Symptoms:** Errors about missing columns or tables

**Solutions:**
1. Delete the database and reinitialize:
   ```bash
   cd backend
   rm database.db
   python init_db.py
   ```
2. Verify all model imports in `init_db.py` are correct
3. Check that you're using the correct database file (should be `database.db` not `lifeadmin.db`)

### CORS errors

**Symptoms:** Browser console shows CORS errors when making API requests

**Solutions:**
1. Verify `FRONTEND_URL` is set in `backend/.env`:
   ```env
   FRONTEND_URL=http://localhost:5173  # For development
   FRONTEND_URL=https://yourdomain.com  # For production
   ```
2. Check nginx configuration has proper headers
3. Restart the backend service after changing `.env`:
   ```bash
   sudo systemctl restart lifeadmin-backend
   ```

### Email verification not sending

**Symptoms:** No verification email received after registration

**Solutions:**
1. Check SMTP settings in `backend/.env`:
   - For Gmail, use port 587 and an App Password
   - Verify `SMTP_USER` and `SMTP_PASSWORD` are correct
2. Check backend logs for email errors:
   ```bash
   sudo journalctl -u lifeadmin-backend -f | grep -i email
   ```
3. Check spam folder
4. Test email configuration:
   ```bash
   # Run a test email (you can create a test script)
   python -c "import aiosmtplib; print('aiosmtplib available')"
   ```

### Port already in use

**Symptoms:** Error starting backend: "Address already in use"

**Solutions:**
1. Find and kill the process using port 8000:
   ```bash
   lsof -i :8000
   kill -9 <PID>
   ```
2. Or use a different port:
   ```bash
   uvicorn main:app --reload --port 8001
   ```

### Frontend not loading

**Symptoms:** Blank page or 404 errors

**Solutions:**
1. Verify the build was successful:
   ```bash
   cd frontend
   npm run build
   ls -la dist/  # Should show index.html and assets/
   ```
2. Check nginx configuration points to correct path
3. Verify nginx can read the dist directory:
   ```bash
   sudo chmod -R 755 /home/lifeadmin/LifeAdmin/frontend/dist
   ```
4. Restart nginx:
   ```bash
   sudo systemctl restart nginx
   ```

## Database Schema

### User Table

Fields include:
- **Authentication:** `id`, `email`, `password_hash`, `full_name`
- **Email Verification:** `email_verified`, `email_verified_at`
- **OAuth:** `google_id`, `profile_picture`
- **Tokens:** `token`, `refresh_token`, `refresh_token_expires`
- **Notification Preferences:** `email_notifications`, `notification_days_before`, `daily_digest`
- **Display Preferences:** `date_format`, `time_format`, `items_per_page`, `default_sort`
- **Account Settings:** `language`, `timezone`
- **Subscription:** `stripe_customer_id`, `stripe_subscription_id`, `subscription_status`, `subscription_plan`, `subscription_current_period_end`
- **Timestamps:** `created_at`, `updated_at`

### Items Table

Fields for managing documents and subscriptions:
- `name`, `category`, `type` (document/subscription)
- `item_type_id`, `item_type_name` (references ItemType)
- Legacy fields: `expiration_date`, `document_number`, `renewal_date`, `billing_cycle`, `price`
- `dynamic_fields` (JSON) - for flexible field storage
- `file_path`, `notes`
- `reminder_days_before` (custom reminder schedule)
- `user_id` (foreign key)
- `created_at`, `updated_at`

### ItemType Table

Template definitions for item types:
- `name`, `category`, `item_class`
- `description`, `icon`
- `fields_config` (JSON) - field definitions
- `is_active`
- `created_at`, `updated_at`

### Notification Table

User notifications:
- `user_id`, `item_id` (foreign keys)
- `title`, `message`, `notification_type`
- `is_read`, `is_sent_via_email`
- `created_at`, `read_at`

## Security Best Practices

1. **Always use HTTPS in production**
   - Set `SECURE_COOKIES=true` in backend `.env`
   - Use certbot for free SSL certificates

2. **Generate a strong SECRET_KEY**
   ```bash
   openssl rand -hex 32
   ```

3. **Use App Passwords for Gmail**
   - Never use your main Google account password
   - Create an App Password at: https://myaccount.google.com/apppasswords

4. **Keep dependencies updated**
   ```bash
   cd backend
   pip list --outdated
   pip install --upgrade <package>
   ```

5. **Regular backups**
   ```bash
   # Backup database
   cp backend/database.db backend/database.db.backup-$(date +%Y%m%d)
   
   # Backup uploaded files
   tar -czf uploads-backup-$(date +%Y%m%d).tar.gz backend/uploads/
   ```

6. **Monitor logs**
   ```bash
   sudo journalctl -u lifeadmin-backend -f
   ```

## Development Tips

### Running tests

```bash
# Backend tests
cd backend
pip install pytest httpx
pytest tests/

# Frontend tests
cd frontend
npm install
npm test

# Run tests in watch mode (frontend)
npm run test:watch

# Run tests with coverage (frontend)
npm run test:coverage
```

### Database inspection

```bash
# Open database with SQLite CLI
sqlite3 backend/database.db

# List all tables
.tables

# View user table schema
.schema user

# Query users
SELECT id, email, email_verified, google_id FROM user;

# Exit
.quit
```

### Viewing logs

```bash
# Backend application logs
tail -f backend/app.log

# System service logs
sudo journalctl -u lifeadmin-backend -f

# Nginx access logs
sudo tail -f /var/log/nginx/access.log

# Nginx error logs
sudo tail -f /var/log/nginx/error.log
```

## Getting Help

If you encounter issues not covered in this guide:

1. Check the backend logs: `sudo journalctl -u lifeadmin-backend -f`
2. Check nginx logs: `sudo tail -f /var/log/nginx/error.log`
3. Review the backend app log: `tail -f backend/app.log`
4. Verify all environment variables are set correctly
5. Ensure all services are running: `sudo systemctl status lifeadmin-backend nginx`

## Next Steps

After successful setup:

1. **Configure email templates** - Customize verification and notification emails
2. **Set up Stripe** (optional) - Enable premium subscriptions
3. **Add item types** - Create templates for common document/subscription types
4. **Configure notifications** - Set up daily digest emails
5. **Backup strategy** - Set up automated backups for database and uploaded files
