# backend/routes/payments.py
from fastapi import APIRouter, Depends, HTTPException, Request, Header
from fastapi.responses import JSONResponse
from sqlmodel import Session, select
from typing import Optional
import os
import logging
import stripe

from models.user import User
from database import get_session
from utils.auth import get_current_user

router = APIRouter(prefix="/payments", tags=["Payments"])
logger = logging.getLogger(__name__)

# Initialize Stripe
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
STRIPE_PRICE_ID_PREMIUM = os.getenv("STRIPE_PRICE_ID_PREMIUM")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")


@router.get("/config")
def get_stripe_config():
    """Get Stripe publishable key for frontend (public endpoint)"""
    return {
        "publishableKey": os.getenv("STRIPE_PUBLISHABLE_KEY")
    }


@router.post("/create-checkout-session")
async def create_checkout_session(
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    """Create a Stripe checkout session for Premium subscription"""
    try:
        # Create or retrieve Stripe customer
        if user.stripe_customer_id:
            customer_id = user.stripe_customer_id
        else:
            customer = stripe.Customer.create(
                email=user.email,
                name=user.full_name,
                metadata={
                    "user_id": str(user.id)
                }
            )
            customer_id = customer.id
            
            # Update user with customer ID
            user.stripe_customer_id = customer_id
            session.add(user)
            session.commit()
            logger.info(f"✅ Created Stripe customer {customer_id} for user {user.email}")
        
        # Create checkout session
        checkout_session = stripe.checkout.Session.create(
            customer=customer_id,
            mode="subscription",
            payment_method_types=["card"],
            line_items=[{
                "price": STRIPE_PRICE_ID_PREMIUM,
                "quantity": 1,
            }],
            success_url=f"{FRONTEND_URL}/subscription?success=true",
            cancel_url=f"{FRONTEND_URL}/subscription?canceled=true",
            metadata={
                "user_id": str(user.id)
            }
        )
        
        logger.info(f"✅ Created checkout session for user {user.email}")
        return {"url": checkout_session.url}
        
    except stripe.error.StripeError as e:
        logger.error(f"❌ Stripe error: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Stripe error: {str(e)}")
    except Exception as e:
        logger.error(f"❌ Error creating checkout session: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to create checkout session")


@router.post("/create-portal-session")
async def create_portal_session(
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    """Create a Stripe customer portal session for subscription management"""
    try:
        if not user.stripe_customer_id:
            raise HTTPException(
                status_code=400, 
                detail="No subscription found. Please subscribe first."
            )
        
        portal_session = stripe.billing_portal.Session.create(
            customer=user.stripe_customer_id,
            return_url=f"{FRONTEND_URL}/subscription"
        )
        
        logger.info(f"✅ Created portal session for user {user.email}")
        return {"url": portal_session.url}
        
    except stripe.error.StripeError as e:
        logger.error(f"❌ Stripe error: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Stripe error: {str(e)}")
    except Exception as e:
        logger.error(f"❌ Error creating portal session: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to create portal session")


@router.post("/webhooks/stripe")
async def stripe_webhook(
    request: Request,
    stripe_signature: Optional[str] = Header(None),
    session: Session = Depends(get_session)
):
    """Handle Stripe webhook events"""
    try:
        payload = await request.body()
        
        # Verify webhook signature
        if STRIPE_WEBHOOK_SECRET:
            try:
                event = stripe.Webhook.construct_event(
                    payload, stripe_signature, STRIPE_WEBHOOK_SECRET
                )
            except stripe.error.SignatureVerificationError as e:
                logger.error(f"❌ Webhook signature verification failed: {str(e)}")
                raise HTTPException(status_code=400, detail="Invalid signature")
        else:
            # For development/testing without webhook secret
            import json
            event = json.loads(payload)
            logger.warning("⚠️ Processing webhook without signature verification")
        
        event_type = event["type"]
        data = event["data"]["object"]
        
        logger.info(f"📥 Received Stripe webhook: {event_type}")
        
        # Handle different event types
        if event_type == "checkout.session.completed":
            await handle_checkout_completed(data, session)
        
        elif event_type == "customer.subscription.created":
            await handle_subscription_created(data, session)
        
        elif event_type == "customer.subscription.updated":
            await handle_subscription_updated(data, session)
        
        elif event_type == "customer.subscription.deleted":
            await handle_subscription_deleted(data, session)
        
        elif event_type == "invoice.payment_succeeded":
            await handle_invoice_payment_succeeded(data, session)
        
        elif event_type == "invoice.payment_failed":
            await handle_invoice_payment_failed(data, session)
        
        else:
            logger.info(f"ℹ️ Unhandled event type: {event_type}")
        
        return JSONResponse({"status": "success"})
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Error processing webhook: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Webhook processing failed")


async def handle_checkout_completed(data: dict, session: Session):
    """Handle successful checkout session"""
    customer_id = data.get("customer")
    subscription_id = data.get("subscription")
    
    # Find user by customer ID
    statement = select(User).where(User.stripe_customer_id == customer_id)
    user = session.exec(statement).first()
    
    if user:
        user.stripe_subscription_id = subscription_id
        session.add(user)
        session.commit()
        logger.info(f"✅ Updated user {user.email} with subscription {subscription_id}")
    else:
        logger.warning(f"⚠️ User not found for customer {customer_id}")


async def handle_subscription_created(data: dict, session: Session):
    """Handle subscription creation"""
    customer_id = data.get("customer")
    subscription_id = data.get("id")
    status = data.get("status")
    current_period_end = data.get("current_period_end")
    
    # Find user by customer ID
    statement = select(User).where(User.stripe_customer_id == customer_id)
    user = session.exec(statement).first()
    
    if user:
        user.stripe_subscription_id = subscription_id
        user.subscription_status = status
        user.subscription_plan = "premium"
        if current_period_end:
            from datetime import datetime
            user.subscription_current_period_end = datetime.fromtimestamp(current_period_end)
        
        session.add(user)
        session.commit()
        logger.info(f"✅ Activated premium subscription for {user.email}")
    else:
        logger.warning(f"⚠️ User not found for customer {customer_id}")


async def handle_subscription_updated(data: dict, session: Session):
    """Handle subscription updates"""
    customer_id = data.get("customer")
    status = data.get("status")
    current_period_end = data.get("current_period_end")
    
    # Find user by customer ID
    statement = select(User).where(User.stripe_customer_id == customer_id)
    user = session.exec(statement).first()
    
    if user:
        user.subscription_status = status
        if current_period_end:
            from datetime import datetime
            user.subscription_current_period_end = datetime.fromtimestamp(current_period_end)
        
        session.add(user)
        session.commit()
        logger.info(f"✅ Updated subscription status for {user.email}: {status}")
    else:
        logger.warning(f"⚠️ User not found for customer {customer_id}")


async def handle_subscription_deleted(data: dict, session: Session):
    """Handle subscription cancellation"""
    customer_id = data.get("customer")
    
    # Find user by customer ID
    statement = select(User).where(User.stripe_customer_id == customer_id)
    user = session.exec(statement).first()
    
    if user:
        user.subscription_status = "canceled"
        user.subscription_plan = "free"
        user.stripe_subscription_id = None
        
        session.add(user)
        session.commit()
        logger.info(f"✅ Canceled subscription for {user.email}")
    else:
        logger.warning(f"⚠️ User not found for customer {customer_id}")


async def handle_invoice_payment_succeeded(data: dict, session: Session):
    """Handle successful invoice payment"""
    customer_id = data.get("customer")
    period_end = data.get("lines", {}).get("data", [{}])[0].get("period", {}).get("end")
    
    # Find user by customer ID
    statement = select(User).where(User.stripe_customer_id == customer_id)
    user = session.exec(statement).first()
    
    if user:
        if period_end:
            from datetime import datetime
            user.subscription_current_period_end = datetime.fromtimestamp(period_end)
        
        session.add(user)
        session.commit()
        logger.info(f"✅ Updated billing period for {user.email}")
    else:
        logger.warning(f"⚠️ User not found for customer {customer_id}")


async def handle_invoice_payment_failed(data: dict, session: Session):
    """Handle failed invoice payment"""
    customer_id = data.get("customer")
    
    # Find user by customer ID
    statement = select(User).where(User.stripe_customer_id == customer_id)
    user = session.exec(statement).first()
    
    if user:
        user.subscription_status = "past_due"
        session.add(user)
        session.commit()
        logger.warning(f"⚠️ Payment failed for {user.email}, status set to past_due")
    else:
        logger.warning(f"⚠️ User not found for customer {customer_id}")
