"""
Email sending functions for authentication
"""
import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logger = logging.getLogger(__name__)


def send_password_reset_email(to_email: str, user_name: str, reset_link: str):
    """Send password reset email"""
    smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER", "")
    smtp_password = os.getenv("SMTP_PASSWORD", "")
    from_email = os.getenv("FROM_EMAIL", smtp_user)
    
    if not smtp_user or not smtp_password:
        logger.info(f"\n{'='*60}\n📧 PASSWORD RESET EMAIL (SMTP not configured)\n{'='*60}\nTo: {to_email}\nReset Link: {reset_link}\n{'='*60}\n")
        return
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Reset Your LifeAdmin Password'
    msg['From'] = from_email
    msg['To'] = to_email
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background: linear-gradient(135deg, #14b8a6 0%, #06b6d4 100%); 
                       color: white; padding: 30px; text-align: center; border-radius: 10px 10px 0 0; }}
            .content {{ background: #f9f9f9; padding: 30px; border-radius: 0 0 10px 10px; }}
            .button {{ display: inline-block; padding: 15px 30px; background: linear-gradient(135deg, #14b8a6 0%, #06b6d4 100%); 
                       color: white; text-decoration: none; border-radius: 8px; font-weight: bold; margin: 20px 0; }}
            .footer {{ text-align: center; margin-top: 20px; color: #666; font-size: 12px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🔑 Password Reset Request</h1>
            </div>
            <div class="content">
                <p>Hi {user_name},</p>
                <p>We received a request to reset your LifeAdmin password. Click the button below to create a new password:</p>
                <div style="text-align: center;">
                    <a href="{reset_link}" class="button">Reset Password</a>
                </div>
                <p>Or copy and paste this link into your browser:</p>
                <p style="background: white; padding: 15px; border-radius: 5px; word-break: break-all; font-size: 14px;">
                    {reset_link}
                </p>
                <p><strong>⏰ This link will expire in 1 hour.</strong></p>
                <p>If you didn't request a password reset, you can safely ignore this email.</p>
                <p>Best regards,<br>The LifeAdmin Team</p>
            </div>
            <div class="footer">
                <p>This is an automated email. Please do not reply.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    msg.attach(MIMEText(html, 'html'))
    
    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
        logger.info(f"✅ Password reset email sent to {to_email}")
    except Exception as e:
        logger.error(f"❌ Failed to send email: {e}")


def send_verification_email(to_email: str, user_name: str, verification_link: str):
    """Send email verification link"""
    smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER", "")
    smtp_password = os.getenv("SMTP_PASSWORD", "")
    from_email = os.getenv("FROM_EMAIL", smtp_user)
    
    if not smtp_user or not smtp_password:
        logger.info(f"\n{'='*60}\n📧 EMAIL VERIFICATION (SMTP not configured)\n{'='*60}\nTo: {to_email}\nVerification Link: {verification_link}\n{'='*60}\n")
        return
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Verify Your LifeAdmin Email Address'
    msg['From'] = from_email
    msg['To'] = to_email
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background: linear-gradient(135deg, #14b8a6 0%, #06b6d4 100%); 
                       color: white; padding: 30px; text-align: center; border-radius: 10px 10px 0 0; }}
            .content {{ background: #f9f9f9; padding: 30px; border-radius: 0 0 10px 10px; }}
            .button {{ display: inline-block; padding: 15px 30px; background: linear-gradient(135deg, #14b8a6 0%, #06b6d4 100%); 
                       color: white; text-decoration: none; border-radius: 8px; font-weight: bold; margin: 20px 0; }}
            .footer {{ text-align: center; margin-top: 20px; color: #666; font-size: 12px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>✉️ Verify Your Email</h1>
            </div>
            <div class="content">
                <p>Hi {user_name},</p>
                <p>Welcome to LifeAdmin! Please verify your email address to get started:</p>
                <div style="text-align: center;">
                    <a href="{verification_link}" class="button">Verify Email Address</a>
                </div>
                <p>Or copy and paste this link into your browser:</p>
                <p style="background: white; padding: 15px; border-radius: 5px; word-break: break-all; font-size: 14px;">
                    {verification_link}
                </p>
                <p><strong>⏰ This link will expire in 24 hours.</strong></p>
                <p>If you didn't create an account, you can safely ignore this email.</p>
                <p>Best regards,<br>The LifeAdmin Team</p>
            </div>
            <div class="footer">
                <p>This is an automated email. Please do not reply.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    msg.attach(MIMEText(html, 'html'))
    
    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
        logger.info(f"✅ Verification email sent to {to_email}")
    except Exception as e:
        logger.error(f"❌ Failed to send email: {e}")
