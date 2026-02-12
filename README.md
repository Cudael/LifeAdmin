# LifeAdmin

A modern document and subscription management system built with FastAPI and Vue.js.

## Features

- 📄 Document management with file uploads
- 💳 Subscription tracking and renewal reminders
- 🔐 Secure authentication with JWT
- ✉️ Email verification
- 🔑 Google OAuth integration
- 📊 Dashboard with statistics
- 🔔 Email notifications (coming soon)

## Tech Stack

**Backend:**
- FastAPI (Python)
- SQLModel + SQLite
- JWT Authentication
- Email verification

**Frontend:**
- Vue 3 + Vite
- TailwindCSS
- Lucide Icons
- Vue Router

## Prerequisites

- Python 3.9+
- Node.js 16+
- npm or yarn

## Installation

### 1. Clone the repository

\`\`\`bash
git clone https://github.com/YOUR_USERNAME/lifeadmin.git
cd lifeadmin
\`\`\`

### 2. Backend Setup

\`\`\`bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Edit .env and fill in your values
# At minimum, set SECRET_KEY (see .env.example for how to generate)

# Run database migrations
python migrate.py

# Start the backend
uvicorn main:app --reload
\`\`\`

Backend will run at: http://localhost:8000

### 3. Frontend Setup

\`\`\`bash
cd frontend

# Install dependencies
npm install

# Copy environment template
cp .env.example .env

# Start the frontend
npm run dev
\`\`\`

Frontend will run at: http://localhost:5173

## Environment Variables

See `.env.example` files in `backend/` and `frontend/` directories for required environment variables.

### Required Backend Variables:
- `SECRET_KEY` - JWT secret (generate with: `python -c "import secrets; print(secrets.token_urlsafe(32))"`)
- `FRONTEND_URL` - Frontend URL for CORS

### Optional Backend Variables:
- `GOOGLE_CLIENT_ID` / `GOOGLE_CLIENT_SECRET` - For Google OAuth
- `SMTP_*` - For email verification and notifications

## API Documentation

Once the backend is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

\`\`\`
lifeadmin/
├── backend/
│   ├── models/          # Database models
│   ├── routes/          # API endpoints
│   ├── utils/           # Helper functions
│   ├── main.py          # FastAPI app
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/  # Vue components
│   │   ├── pages/       # Page components
│   │   ├── layouts/     # Layout components
│   │   └── utils/       # Helper functions
│   └── package.json
└── README.md
\`\`\`

## Security

### Best Practices

**Required:**
- Never commit `.env` files to version control
- Use a strong, randomly generated `SECRET_KEY` in production (32+ characters)
  - Generate with: `python -c "import secrets; print(secrets.token_urlsafe(32))"`
- Enable `SECURE_COOKIES=true` in production when using HTTPS
- Keep all dependencies up to date
- Use strong passwords (minimum 8 characters with uppercase, lowercase, numbers, and special characters)

**Recommended for Production:**
- Use HTTPS (TLS/SSL) for all connections
- Enable HSTS (Strict-Transport-Security) headers
- Set up regular database backups
- Monitor logs for suspicious activity
- Use environment-specific configurations
- Implement proper firewall rules
- Consider using a Web Application Firewall (WAF)
- Regularly audit user access and permissions

**Security Features Included:**
- JWT token-based authentication with 30-minute expiration
- Password hashing with bcrypt
- Email verification system
- Rate limiting on sensitive endpoints (login, registration, file uploads)
- File upload validation (extension and MIME type checking)
- Input validation and sanitization
- Security headers (X-Content-Type-Options, X-Frame-Options, etc.)
- SQL injection protection via parameterized queries (SQLModel/SQLAlchemy)
- CORS configuration for cross-origin requests

**Reporting Security Issues:**
Please report security vulnerabilities privately to the repository maintainers via GitHub Security Advisories.

## License

MIT

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

## Support

For issues or questions, please open a GitHub issue.