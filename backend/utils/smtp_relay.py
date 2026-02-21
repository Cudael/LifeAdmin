# utils/smtp_relay.py
"""
Reusable email-sending module using Google Workspace SMTP Relay.

Uses smtp-relay.gmail.com on port 587 with TLS.
IP-authenticated (no username/password required).
Supports sending from Remindes aliases:
  - support@remindes.com
  - info@remindes.com
  - no-reply@remindes.com
  - billing@remindes.com
"""
import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logger = logging.getLogger(__name__)

SMTP_RELAY_HOST = os.getenv("SMTP_RELAY_HOST", "smtp-relay.gmail.com")
SMTP_RELAY_PORT = int(os.getenv("SMTP_RELAY_PORT", "587"))
SMTP_FROM_NAME = os.getenv("SMTP_FROM_NAME", "Remindes")

VALID_FROM_ADDRESSES = [
    "support@remindes.com",
    "info@remindes.com",
    "no-reply@remindes.com",
    "billing@remindes.com",
]


def send_email(
    to_email: str,
    subject: str,
    html_body: str,
    from_email: str = "no-reply@remindes.com",
    from_name: str | None = None,
    plain_body: str | None = None,
) -> bool:
    """
    Send an email via Google Workspace SMTP Relay.

    Args:
        to_email: Recipient email address.
        subject: Email subject line.
        html_body: HTML content of the email.
        from_email: Sender address (must be a valid Remindes alias).
        from_name: Display name for the sender. Defaults to SMTP_FROM_NAME.
        plain_body: Optional plain-text fallback. If omitted, only HTML is sent.

    Returns:
        True if the email was sent successfully, False otherwise.
    """
    if from_email not in VALID_FROM_ADDRESSES:
        logger.error(f"Invalid from_email '{from_email}'. Must be one of {VALID_FROM_ADDRESSES}")
        return False

    sender_name = from_name or SMTP_FROM_NAME

    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = f"{sender_name} <{from_email}>"
        msg["To"] = to_email

        if plain_body:
            msg.attach(MIMEText(plain_body, "plain"))
        msg.attach(MIMEText(html_body, "html"))

        with smtplib.SMTP(SMTP_RELAY_HOST, SMTP_RELAY_PORT) as server:
            server.starttls()
            # IP-authenticated – no login required
            server.send_message(msg)

        logger.info(f"✅ Email sent to {to_email} from {from_email} (subject: {subject})")
        return True

    except Exception as e:
        logger.error(f"❌ Failed to send email to {to_email}: {e}")
        return False
