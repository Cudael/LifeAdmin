"""
Email sending functions for authentication
"""
import logging

from utils.smtp_relay import send_email

logger = logging.getLogger(__name__)


def send_password_reset_email(to_email: str, user_name: str, reset_link: str):
    """Send password reset email"""

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
                <p>We received a request to reset your Remindes password. Click the button below to create a new password:</p>
                <div style="text-align: center;">
                    <a href="{reset_link}" class="button">Reset Password</a>
                </div>
                <p>Or copy and paste this link into your browser:</p>
                <p style="background: white; padding: 15px; border-radius: 5px; word-break: break-all; font-size: 14px;">
                    {reset_link}
                </p>
                <p><strong>⏰ This link will expire in 1 hour.</strong></p>
                <p>If you didn't request a password reset, you can safely ignore this email.</p>
                <p>Best regards,<br>The Remindes Team</p>
            </div>
            <div class="footer">
                <p>This is an automated email. Please do not reply.</p>
            </div>
        </div>
    </body>
    </html>
    """

    result = send_email(
        to_email=to_email,
        subject="Reset Your Remindes Password",
        html_body=html,
        from_email="no-reply@remindes.com",
    )
    if result:
        logger.info(f"✅ Password reset email sent to {to_email}")
    else:
        logger.error(f"❌ Failed to send password reset email to {to_email}")


def send_verification_email(to_email: str, user_name: str, verification_link: str):
    """Send email verification link"""

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
                <p>Welcome to Remindes! Please verify your email address to get started:</p>
                <div style="text-align: center;">
                    <a href="{verification_link}" class="button">Verify Email Address</a>
                </div>
                <p>Or copy and paste this link into your browser:</p>
                <p style="background: white; padding: 15px; border-radius: 5px; word-break: break-all; font-size: 14px;">
                    {verification_link}
                </p>
                <p><strong>⏰ This link will expire in 24 hours.</strong></p>
                <p>If you didn't create an account, you can safely ignore this email.</p>
                <p>Best regards,<br>The Remindes Team</p>
            </div>
            <div class="footer">
                <p>This is an automated email. Please do not reply.</p>
            </div>
        </div>
    </body>
    </html>
    """

    result = send_email(
        to_email=to_email,
        subject="Verify Your Remindes Email Address",
        html_body=html,
        from_email="no-reply@remindes.com",
    )
    if result:
        logger.info(f"✅ Verification email sent to {to_email}")
    else:
        logger.error(f"❌ Failed to send verification email to {to_email}")
