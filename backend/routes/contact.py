"""
Contact form endpoint
"""
import html as html_module
import logging
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, EmailStr
from slowapi import Limiter
from slowapi.util import get_remote_address

from utils.smtp_relay import send_email

router = APIRouter(prefix="/contact", tags=["contact"])
limiter = Limiter(key_func=get_remote_address)
logger = logging.getLogger(__name__)

NAME_MIN_LENGTH = 2
NAME_MAX_LENGTH = 100
MESSAGE_MIN_LENGTH = 10
MESSAGE_MAX_LENGTH = 5000

INQUIRY_ROUTING = {
    "Technical Support": "support@remindes.com",
    "Billing Question": "billing@remindes.com",
    "Enterprise Sales": "info@remindes.com",
    "Feature Request": "info@remindes.com",
    "Other": "support@remindes.com",
}

VALID_INQUIRY_TYPES = list(INQUIRY_ROUTING.keys())


class ContactRequest(BaseModel):
    name: str
    email: EmailStr
    type: str
    message: str


@router.post("/")
@limiter.limit("5/hour")
async def submit_contact_form(request: Request, data: ContactRequest):
    """Handle contact form submission"""

    name = data.name.strip()
    email = str(data.email).strip().lower()
    inquiry_type = data.type.strip()
    message = data.message.strip()

    if not name or len(name) < NAME_MIN_LENGTH:
        raise HTTPException(status_code=400, detail=f"Name must be at least {NAME_MIN_LENGTH} characters")
    if len(name) > NAME_MAX_LENGTH:
        raise HTTPException(status_code=400, detail=f"Name must not exceed {NAME_MAX_LENGTH} characters")
    if not message or len(message) < MESSAGE_MIN_LENGTH:
        raise HTTPException(status_code=400, detail=f"Message must be at least {MESSAGE_MIN_LENGTH} characters")
    if len(message) > MESSAGE_MAX_LENGTH:
        raise HTTPException(status_code=400, detail=f"Message must not exceed {MESSAGE_MAX_LENGTH} characters")
    if inquiry_type not in VALID_INQUIRY_TYPES:
        raise HTTPException(status_code=400, detail=f"Invalid inquiry type. Must be one of: {', '.join(VALID_INQUIRY_TYPES)}")

    to_email = INQUIRY_ROUTING[inquiry_type]

    safe_name = html_module.escape(name)
    safe_email = html_module.escape(email)
    safe_inquiry_type = html_module.escape(inquiry_type)
    safe_message = html_module.escape(message)

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background: linear-gradient(135deg, #14b8a6 0%, #06b6d4 100%);
                       color: white; padding: 20px; text-align: center; border-radius: 10px 10px 0 0; }}
            .content {{ background: #f9f9f9; padding: 30px; border-radius: 0 0 10px 10px; }}
            .field {{ margin-bottom: 15px; }}
            .label {{ font-weight: bold; color: #555; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>New Contact Form Submission</h2>
            </div>
            <div class="content">
                <div class="field">
                    <span class="label">Name:</span> {safe_name}
                </div>
                <div class="field">
                    <span class="label">Email:</span> {safe_email}
                </div>
                <div class="field">
                    <span class="label">Inquiry Type:</span> {safe_inquiry_type}
                </div>
                <div class="field">
                    <span class="label">Message:</span>
                    <p>{safe_message}</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    plain = f"Name: {name}\nEmail: {email}\nType: {inquiry_type}\n\nMessage:\n{message}"

    success = send_email(
        to_email=to_email,
        subject=f"[Remindes Contact] {inquiry_type} from {name}",
        html_body=html,
        from_email="support@remindes.com",
        plain_body=plain,
    )

    if not success:
        logger.error(f"Failed to send contact form email from {email}")
        raise HTTPException(status_code=500, detail="Failed to send message. Please try again later.")

    logger.info(f"✅ Contact form submitted: {inquiry_type} from {email} -> {to_email}")
    return {"success": True, "message": "Message sent successfully. We'll be in touch."}
