# utils/email_service.py
import os
from datetime import date

from utils.smtp_relay import send_email

def send_expiry_notification_email(
    to_email: str,
    user_name: str,
    item_name: str,
    item_type: str,
    expiry_date: date,
    days_until_expiry: int
):
    """Send an expiry notification email"""
    
    subject = f"⚠️ {item_name} expiring in {days_until_expiry} day{'s' if days_until_expiry != 1 else ''}"
    
    # Plain text version
    text = f"""
Hello {user_name},

This is a reminder that your {item_type} "{item_name}" is expiring soon.

Expiry Date: {expiry_date.strftime('%B %d, %Y')}
Days Remaining: {days_until_expiry} day{'s' if days_until_expiry != 1 else ''}

Please take action to renew or update this item.

---
Remindes - Never miss an important date
    """

    # HTML version
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }}
        .container {{
            background: linear-gradient(135deg, #14b8a6 0%, #06b6d4 100%);
            border-radius: 16px;
            padding: 1px;
            margin: 20px 0;
        }}
        .content {{
            background: white;
            border-radius: 15px;
            padding: 30px;
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
        }}
        .logo {{
            font-size: 28px;
            font-weight: bold;
            background: linear-gradient(135deg, #14b8a6 0%, #06b6d4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        .alert-box {{
            background: #fef3c7;
            border-left: 4px solid #f59e0b;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
        }}
        .alert-title {{
            font-size: 20px;
            font-weight: bold;
            color: #92400e;
            margin-bottom: 10px;
        }}
        .item-details {{
            background: #f3f4f6;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
        }}
        .detail-row {{
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid #e5e7eb;
        }}
        .detail-row:last-child {{
            border-bottom: none;
        }}
        .detail-label {{
            font-weight: 600;
            color: #6b7280;
        }}
        .detail-value {{
            color: #111827;
            font-weight: 500;
        }}
        .days-remaining {{
            font-size: 32px;
            font-weight: bold;
            color: #f59e0b;
            text-align: center;
            margin: 20px 0;
        }}
        .footer {{
            text-align: center;
            color: #6b7280;
            font-size: 14px;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #e5e7eb;
        }}
        .button {{
            display: inline-block;
            background: linear-gradient(135deg, #14b8a6 0%, #06b6d4 100%);
            color: white;
            padding: 12px 30px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            margin: 20px 0;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="content">
            <div class="header">
                <div class="logo">✨ Remindes</div>
                <p style="color: #6b7280; margin-top: 5px;">Never miss an important date</p>
            </div>
            
            <div class="alert-box">
                <div class="alert-title">⚠️ Expiry Warning</div>
                <p style="margin: 0; color: #92400e;">Your {item_type} is expiring soon and needs your attention.</p>
            </div>
            
            <p>Hello <strong>{user_name}</strong>,</p>
            
            <p>This is a friendly reminder about an upcoming expiry:</p>
            
            <div class="item-details">
                <div class="detail-row">
                    <span class="detail-label">Item Name:</span>
                    <span class="detail-value">{item_name}</span>
                </div>
                <div class="detail-row">
                    <span class="detail-label">Type:</span>
                    <span class="detail-value">{item_type}</span>
                </div>
                <div class="detail-row">
                    <span class="detail-label">Expiry Date:</span>
                    <span class="detail-value">{expiry_date.strftime('%B %d, %Y')}</span>
                </div>
            </div>
            
            <div class="days-remaining">
                {days_until_expiry} day{'s' if days_until_expiry != 1 else ''} remaining
            </div>
            
            <p style="text-align: center;">
                <a href="{os.getenv('FRONTEND_URL', 'http://localhost:5173')}/dashboard" class="button">
                    View in Dashboard
                </a>
            </p>
            
            <p style="color: #6b7280;">Please take action to renew or update this item before it expires.</p>
            
            <div class="footer">
                <p>You're receiving this email because you have email notifications enabled in Remindes.</p>
                <p style="margin-top: 10px;">
                    <a href="{os.getenv('FRONTEND_URL', 'http://localhost:5173')}/settings" style="color: #14b8a6;">Manage notification preferences</a>
                </p>
            </div>
        </div>
    </div>
</body>
</html>
    """
    return send_email(
        to_email=to_email,
        subject=subject,
        html_body=html,
        from_email="no-reply@remindes.com",
        plain_body=text,
    )


def send_expired_notification_email(
    to_email: str,
    user_name: str,
    item_name: str,
    item_type: str,
    expiry_date: date,
    days_expired: int
):
    """Send an expired item notification email"""
    
    subject = f"❌ {item_name} has expired"

    # Plain text version
    text = f"""
Hello {user_name},

This is an urgent reminder that your {item_type} "{item_name}" has expired.

Expiry Date: {expiry_date.strftime('%B %d, %Y')}
Days Overdue: {days_expired} day{'s' if days_expired != 1 else ''}

Please take immediate action to renew or update this item.

---
Remindes - Never miss an important date
    """

    # HTML version
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }}
        .container {{
            background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
            border-radius: 16px;
            padding: 1px;
            margin: 20px 0;
        }}
        .content {{
            background: white;
            border-radius: 15px;
            padding: 30px;
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
        }}
        .logo {{
            font-size: 28px;
            font-weight: bold;
            background: linear-gradient(135deg, #14b8a6 0%, #06b6d4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        .alert-box {{
            background: #fee2e2;
            border-left: 4px solid #dc2626;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
        }}
        .alert-title {{
            font-size: 20px;
            font-weight: bold;
            color: #991b1b;
            margin-bottom: 10px;
        }}
        .item-details {{
            background: #f3f4f6;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
        }}
        .detail-row {{
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid #e5e7eb;
        }}
        .detail-row:last-child {{
            border-bottom: none;
        }}
        .detail-label {{
            font-weight: 600;
            color: #6b7280;
        }}
        .detail-value {{
            color: #111827;
            font-weight: 500;
        }}
        .days-expired {{
            font-size: 32px;
            font-weight: bold;
            color: #dc2626;
            text-align: center;
            margin: 20px 0;
        }}
        .footer {{
            text-align: center;
            color: #6b7280;
            font-size: 14px;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #e5e7eb;
        }}
        .button {{
            display: inline-block;
            background: linear-gradient(135deg, #14b8a6 0%, #06b6d4 100%);
            color: white;
            padding: 12px 30px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            margin: 20px 0;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="content">
            <div class="header">
                <div class="logo">✨ Remindes</div>
                <p style="color: #6b7280; margin-top: 5px;">Never miss an important date</p>
            </div>
            
            <div class="alert-box">
                <div class="alert-title">❌ Item Expired</div>
                <p style="margin: 0; color: #991b1b;">Your {item_type} has expired and requires immediate attention.</p>
            </div>
            
            <p>Hello <strong>{user_name}</strong>,</p>
            
            <p>This is an urgent reminder about an expired item:</p>
            
            <div class="item-details">
                <div class="detail-row">
                    <span class="detail-label">Item Name:</span>
                    <span class="detail-value">{item_name}</span>
                </div>
                <div class="detail-row">
                    <span class="detail-label">Type:</span>
                    <span class="detail-value">{item_type}</span>
                </div>
                <div class="detail-row">
                    <span class="detail-label">Expiry Date:</span>
                    <span class="detail-value">{expiry_date.strftime('%B %d, %Y')}</span>
                </div>
            </div>
            
            <div class="days-expired">
                Expired {days_expired} day{'s' if days_expired != 1 else ''} ago
            </div>
            
            <p style="text-align: center;">
                <a href="{os.getenv('FRONTEND_URL', 'http://localhost:5173')}/dashboard" class="button">
                    View in Dashboard
                </a>
            </p>
            
            <p style="color: #6b7280;">Please renew or update this item as soon as possible.</p>
            
            <div class="footer">
                <p>You're receiving this email because you have email notifications enabled in Remindes.</p>
                <p style="margin-top: 10px;">
                    <a href="{os.getenv('FRONTEND_URL', 'http://localhost:5173')}/settings" style="color: #14b8a6;">Manage notification preferences</a>
                </p>
            </div>
        </div>
    </div>
</body>
</html>
    """

    return send_email(
        to_email=to_email,
        subject=subject,
        html_body=html,
        from_email="no-reply@remindes.com",
        plain_body=text,
    )