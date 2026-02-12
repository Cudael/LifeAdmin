# Security Policy

## Overview

LifeAdmin takes security seriously. This document outlines our security practices, known limitations, and how to report vulnerabilities.

## Security Features

### Authentication & Authorization
- **JWT Tokens**: Access tokens expire after 30 minutes (refresh tokens after 30 days)
- **Password Security**: 
  - Bcrypt hashing with salt
  - Password strength requirements (8+ chars, uppercase, lowercase, numbers, special chars)
  - Protection against common/weak passwords
- **Email Verification**: Required before performing write operations
- **OAuth 2.0**: Google OAuth integration for secure third-party authentication

### Rate Limiting
The following endpoints are rate-limited to prevent abuse:
- Registration: 5 attempts per hour
- Login: 10 attempts per minute
- Password reset: 3 attempts per hour
- Email verification resend: 3 attempts per hour
- Item creation: 30 per minute
- Item updates: 30 per minute
- Item deletion: 20 per minute
- File uploads: 20 per minute
- Bulk operations: 10 per minute

### Input Validation
- **File Uploads**:
  - Maximum size: 10MB
  - Allowed extensions: pdf, doc, docx, xls, xlsx, ppt, pptx, jpg, jpeg, png, gif, webp, txt, csv
  - MIME type validation (when python-magic is available)
  - Filename sanitization to prevent directory traversal
  - **Blocked**: Archives (.zip, .rar) to prevent malware distribution
- **Form Data**:
  - Pydantic validation for all API inputs
  - Email format validation
  - Date format validation
  - Numeric range validation (items per page: 5-100, notification days: 0-365)
  - Enum validation for categories, types, languages, timezones

### Security Headers
The API automatically adds the following security headers:
- `X-Content-Type-Options: nosniff` - Prevents MIME type sniffing
- `X-Frame-Options: DENY` - Prevents clickjacking
- `X-XSS-Protection: 1; mode=block` - Enables XSS filter in older browsers
- `Referrer-Policy: strict-origin-when-cross-origin` - Controls referrer information
- `Permissions-Policy` - Restricts access to sensitive features (geolocation, microphone, camera)
- `Strict-Transport-Security` - Enforces HTTPS (when `SECURE_COOKIES=true`)

### CORS Protection
- Configurable allowed origins via `FRONTEND_URL` environment variable
- Credentials support enabled only for specified origins
- Default origins: `http://localhost:5173`, `http://127.0.0.1:5173`

### SQL Injection Protection
- All database queries use parameterized queries via SQLModel/SQLAlchemy
- No raw SQL with user input (except validated migration scripts)

### Logging & Monitoring
- Request/response logging with IP addresses
- Security event logging (failed logins, weak passwords, unauthorized access attempts)
- Error logging with stack traces (not exposed to clients)

## Known Limitations & Recommendations

### CSRF Protection
**Current State**: Uses `SameSite=lax` cookies, which provides basic CSRF protection.

**Limitation**: Not sufficient for APIs accessed from multiple origins.

**Recommendation for Production**:
1. Implement CSRF tokens using `fastapi-csrf-protect` or similar
2. Or switch to a pure token-based approach (no session cookies)

### Password Reset Tokens
**Current State**: Tokens stored in plaintext in database.

**Recommendation**: Hash tokens before storage using bcrypt or SHA-256. Only store the hash and compare hashed tokens during validation.

### Account Lockout
**Current State**: Rate limiting prevents rapid brute force attacks.

**Limitation**: No permanent account lockout after N failed attempts.

**Recommendation**: Implement account lockout after 5-10 failed login attempts, requiring admin or time-based unlock.

### Session Management
**Current State**: Session middleware used for OAuth only.

**Recommendation**: Consider using separate session storage (Redis) for better scalability and security.

### File Storage
**Current State**: Files stored locally in `uploads/` directory.

**Limitation**: No encryption at rest, scalability concerns.

**Recommendation for Production**:
1. Use cloud storage (AWS S3, Google Cloud Storage, Azure Blob)
2. Implement server-side encryption
3. Use presigned URLs for secure access
4. Implement file scanning for malware

### Database Security
**Current State**: SQLite database with no encryption.

**Recommendation for Production**:
1. Switch to PostgreSQL or MySQL with TLS connections
2. Enable database-level encryption
3. Implement regular automated backups
4. Use connection pooling
5. Restrict database user permissions (principle of least privilege)

## Security Best Practices for Deployment

### Environment Variables
- Never commit `.env` files
- Use strong random values for `SECRET_KEY` (32+ bytes)
- Rotate secrets regularly (every 90 days recommended)
- Use different secrets for dev/staging/production

### HTTPS/TLS
- Always use HTTPS in production
- Set `SECURE_COOKIES=true` when using HTTPS
- Use valid SSL certificates (Let's Encrypt, commercial CA)
- Enable HSTS with `includeSubDomains` and `preload`

### Dependencies
- Run `pip audit` regularly to check for vulnerable packages
- Keep all dependencies updated
- Use `pip-audit` or `safety` in CI/CD pipeline

### Monitoring
- Set up log aggregation (ELK, Splunk, Datadog)
- Monitor for suspicious patterns:
  - Multiple failed login attempts
  - Large file uploads
  - Unusual API usage patterns
  - SQL error messages
- Set up alerts for security events

### Backups
- Automated daily database backups
- Test restore procedures regularly
- Store backups securely (encrypted, off-site)
- Implement backup retention policy

### Access Control
- Use principle of least privilege
- Regularly audit user permissions
- Implement IP whitelisting for admin endpoints
- Use a VPN or bastion host for production access

## Reporting a Vulnerability

We take all security reports seriously. If you discover a security vulnerability, please follow these steps:

### DO NOT:
- Open a public GitHub issue
- Disclose the vulnerability publicly before it's fixed
- Exploit the vulnerability beyond what's necessary to demonstrate it

### DO:
1. **Report privately** via GitHub Security Advisories:
   - Go to the repository's Security tab
   - Click "Report a vulnerability"
   - Provide detailed information

2. **Include in your report**:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if you have one)
   - Your contact information (optional)

3. **Response timeline**:
   - We'll acknowledge receipt within 48 hours
   - We'll provide an initial assessment within 1 week
   - We'll work with you to understand and fix the issue
   - We'll credit you in the security advisory (unless you prefer to remain anonymous)

### Scope
Security reports should focus on:
- Authentication/authorization bypass
- SQL injection
- XSS (Cross-Site Scripting)
- CSRF (Cross-Site Request Forgery)
- Remote code execution
- Information disclosure
- Data leakage
- Cryptographic vulnerabilities

Out of scope:
- Social engineering
- Physical security
- DoS attacks (rate limiting is already in place)
- Issues in third-party dependencies (report to those projects)

## Security Update Policy

- **Critical vulnerabilities**: Patched within 24-48 hours
- **High severity**: Patched within 1 week
- **Medium severity**: Patched within 2 weeks
- **Low severity**: Patched in next regular release

Security updates will be announced via:
- GitHub Security Advisories
- Repository releases
- README updates

## Compliance

LifeAdmin is designed with the following regulations in mind:
- **GDPR**: User data deletion, data export, consent management
- **CCPA**: Data access and deletion rights
- **SOC 2**: Logging, access controls, encryption

Note: Full compliance requires proper deployment and operational procedures beyond the application code.

## Security Checklist for Production

Before deploying to production, ensure:

- [ ] `SECRET_KEY` is set to a strong random value
- [ ] `SECURE_COOKIES=true` is enabled
- [ ] HTTPS is properly configured with valid certificates
- [ ] Database is using strong credentials
- [ ] All environment variables are properly set
- [ ] File upload directory has correct permissions (not world-writable)
- [ ] Logs are being collected and monitored
- [ ] Backups are automated and tested
- [ ] Rate limits are appropriate for your use case
- [ ] CORS origins are restricted to your frontend domain(s)
- [ ] Email verification is working correctly
- [ ] Password reset flow is tested
- [ ] Error messages don't expose sensitive information
- [ ] Dependencies are up to date with no known vulnerabilities
- [ ] Security headers are being sent
- [ ] Database backups are encrypted

## Contact

For security-related questions or concerns, please use GitHub's private vulnerability reporting feature or contact the maintainers directly through GitHub.

## Attribution

We appreciate security researchers who report vulnerabilities responsibly. Contributors will be acknowledged in security advisories unless they prefer to remain anonymous.

---

Last updated: 2026-02-12
