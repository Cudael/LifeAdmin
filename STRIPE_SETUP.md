# Stripe Setup Guide

This guide explains how to set up Stripe payment integration for the Remindes application.

## Prerequisites

- Stripe account (sign up at https://stripe.com)
- Access to Stripe Dashboard
- Backend and frontend deployed and running

## Step 1: Get Stripe API Keys

1. Log in to your Stripe Dashboard: https://dashboard.stripe.com
2. Navigate to **Developers** → **API Keys**
3. Copy your keys:
   - **Publishable key** (starts with `pk_test_` for test mode or `pk_live_` for live mode)
   - **Secret key** (starts with `sk_test_` for test mode or `sk_live_` for live mode)

## Step 2: Create a Product and Price

1. In Stripe Dashboard, go to **Products** → **Add Product**
2. Create a product:
   - **Name**: Premium Monthly
   - **Description**: Unlimited items and premium features
   - **Pricing**: Recurring
   - **Price**: €2.99
   - **Billing period**: Monthly
3. After creating, copy the **Price ID** (starts with `price_`)

## Step 3: Configure Backend Environment Variables

Add these variables to `backend/.env`:

```bash
# Stripe API Keys
STRIPE_SECRET_KEY=sk_test_your_secret_key_here
STRIPE_PUBLISHABLE_KEY=pk_test_your_publishable_key_here

# Stripe Price ID
STRIPE_PRICE_ID_PREMIUM=price_your_price_id_here

# Stripe Webhook Secret (will be added after Step 4)
STRIPE_WEBHOOK_SECRET=

# Frontend URL (for redirects)
FRONTEND_URL=https://remindes.com
```

## Step 4: Set Up Webhook

Webhooks allow Stripe to notify your application about subscription events.

### Create Webhook Endpoint

1. Go to **Developers** → **Webhooks** → **Add endpoint**
2. Set **Endpoint URL**: `https://remindes.com/api/payments/webhooks/stripe`
3. Select **API version**: Latest version
4. Select events to listen for:
   - `checkout.session.completed`
   - `customer.subscription.created`
   - `customer.subscription.updated`
   - `customer.subscription.deleted`
   - `invoice.payment_succeeded`
   - `invoice.payment_failed`
5. Click **Add endpoint**
6. Copy the **Signing secret** (starts with `whsec_`)
7. Add it to `backend/.env`:
   ```bash
   STRIPE_WEBHOOK_SECRET=whsec_your_webhook_secret_here
   ```

## Step 5: Configure Frontend Environment Variables

Add this variable to `frontend/.env`:

```bash
VITE_STRIPE_PUBLISHABLE_KEY=pk_test_your_publishable_key_here
```

## Step 6: Run Database Migration

Run the subscription migration to add required database columns:

```bash
cd backend
python migrations/006_add_subscriptions.py
```

## Step 7: Restart Services

Restart your backend and frontend services to load the new environment variables:

```bash
# Restart backend (systemd)
sudo systemctl restart lifeadmin-backend.service

# Rebuild and deploy frontend
cd frontend
npm install
npm run build
# Copy dist/ to your web server
```

## Testing the Integration

### Test Mode

1. Use test credit cards from Stripe:
   - **Success**: 4242 4242 4242 4242
   - **Decline**: 4000 0000 0000 0002
   - Any future expiry date and any 3-digit CVC

2. Test the checkout flow:
   - Click "Upgrade Monthly" on pricing page
   - Complete checkout with test card
   - Verify redirect to subscription page with success message
   - Check database that user's subscription fields are updated

3. Test webhook events:
   - Go to Stripe Dashboard → **Developers** → **Webhooks**
   - Click on your webhook
   - View recent webhook events and their status
   - All events should show "Success"

### Test Webhook Locally (Optional)

Use Stripe CLI to test webhooks on your local machine:

```bash
# Install Stripe CLI
# https://stripe.com/docs/stripe-cli

# Login
stripe login

# Forward webhooks to local backend
stripe listen --forward-to http://localhost:8000/api/payments/webhooks/stripe

# Trigger test events
stripe trigger checkout.session.completed
stripe trigger customer.subscription.created
stripe trigger customer.subscription.deleted
```

## Switching to Live Mode

⚠️ **IMPORTANT**: Only switch to live mode after thorough testing!

1. Get your **live** API keys from Stripe Dashboard (switch to Live mode toggle)
2. Create a **new product** in live mode with the same pricing
3. Update environment variables with live keys:
   ```bash
   STRIPE_SECRET_KEY=sk_live_your_live_secret_key
   STRIPE_PUBLISHABLE_KEY=pk_live_your_live_publishable_key
   STRIPE_PRICE_ID_PREMIUM=price_your_live_price_id
   ```
4. Create a **new webhook** for production URL
5. Update `STRIPE_WEBHOOK_SECRET` with new webhook secret
6. Restart services
7. Test with real credit card (use small amounts first!)

## Monitoring and Troubleshooting

### Check Logs

Backend logs show all Stripe-related events:

```bash
tail -f backend/app.log | grep -i stripe
```

### Common Issues

**Problem**: Webhook signature verification failed
- **Solution**: Check that `STRIPE_WEBHOOK_SECRET` is correct
- **Solution**: Ensure webhook URL matches exactly (https, correct domain)

**Problem**: Checkout session doesn't redirect
- **Solution**: Check `FRONTEND_URL` in backend .env
- **Solution**: Verify success_url and cancel_url in code

**Problem**: Subscription status not updating
- **Solution**: Check webhook events in Stripe Dashboard
- **Solution**: Verify webhook endpoint is receiving events (200 status)
- **Solution**: Check backend logs for errors

**Problem**: User can't create items after upgrade
- **Solution**: Verify subscription_status is "active" in database
- **Solution**: Check subscription_plan is "premium"
- **Solution**: Verify `is_premium()` method logic

## Security Best Practices

1. ✅ **Never commit secrets** to version control
2. ✅ **Use environment variables** for all API keys
3. ✅ **Always verify webhook signatures** (done automatically)
4. ✅ **Use HTTPS** in production (required by Stripe)
5. ✅ **Don't store card details** (handled by Stripe)
6. ✅ **Use Customer Portal** for all subscription management
7. ✅ **Monitor webhook failures** regularly
8. ✅ **Keep logs secure** (may contain sensitive data)

## Stripe Dashboard Resources

- **Payments**: View all payments and their status
- **Customers**: View customer list and subscription status
- **Subscriptions**: Manage active subscriptions
- **Events**: View all webhook events and responses
- **Logs**: View API request logs
- **Reports**: Financial reports and analytics

## Support

- Stripe Documentation: https://stripe.com/docs
- Stripe Support: https://support.stripe.com
- Test Cards: https://stripe.com/docs/testing

## Checklist for Production

- [ ] Test mode working correctly
- [ ] All webhook events tested
- [ ] Item limit enforcement working
- [ ] Customer portal tested
- [ ] Cancellation flow tested
- [ ] Live API keys obtained
- [ ] Live product created
- [ ] Live webhook created
- [ ] Environment variables updated
- [ ] Services restarted
- [ ] End-to-end test with real card
- [ ] Monitoring set up
- [ ] Backup plan for failures
