# Stripe Payment Integration - Deployment Instructions

This document provides step-by-step instructions for deploying the Stripe payment integration to the production environment at https://remindes.com.

## Prerequisites

- SSH access to the production server
- Backend running at `/home/lifeadmin/LifeAdmin/backend`
- Frontend deployed at `/home/lifeadmin/LifeAdmin/frontend/dist`
- Systemd service: `lifeadmin-backend.service`
- Nginx configured with `/api/` proxy to backend

## Step 1: Activate Virtual Environment and Install Dependencies

```bash
# SSH into production server
ssh lifeadmin@remindes.com

# Navigate to backend directory
cd /home/lifeadmin/LifeAdmin/backend

# Activate virtual environment
source venv/bin/activate

# Install new dependencies (stripe package)
pip install -r requirements.txt
```

## Step 2: Update Backend Environment Variables

Edit the backend `.env` file:

```bash
nano /home/lifeadmin/LifeAdmin/backend/.env
```

Add these Stripe configuration variables:

```bash
# Stripe Configuration
STRIPE_SECRET_KEY=sk_test_51T0c0A0eEDO9PGJfycnmNlJfHKiAumOFmebEmDHbF0im9ngeckYXFiPwpMwtyWLVx4X8dv2KzqEdppNcOkosQamP00TGIfgyZK
STRIPE_PUBLISHABLE_KEY=pk_test_51T0c0A0eEDO9PGJfpRN8BuAPCcDPVg4HY1pbKhMXrmAtIuvfutGHu48RhRzTbJVN4Y30K7P30GpSRV1k8TuWTn0C00OwrgK6Vx
STRIPE_PRICE_ID_PREMIUM=price_1T1RGP0eEDO9PGJfdTfPDX2y
STRIPE_WEBHOOK_SECRET=

# Update Frontend URL if not already set
FRONTEND_URL=https://remindes.com
```

Save and exit (Ctrl+X, Y, Enter)

## Step 3: Run Database Migration

```bash
cd /home/lifeadmin/LifeAdmin/backend

# Run the subscription migration
python migrations/006_add_subscriptions.py
```

Expected output:
```
✅ Added column: stripe_customer_id
✅ Added column: stripe_subscription_id
✅ Added column: subscription_status
✅ Added column: subscription_plan
✅ Added column: subscription_current_period_end
✅ Set subscription_plan to 'free' for X existing users
✅ Created index on stripe_customer_id
🎉 Migration complete!
```

## Step 4: Restart Backend Service

```bash
# Restart the systemd service
sudo systemctl restart lifeadmin-backend.service

# Check service status
sudo systemctl status lifeadmin-backend.service

# Check logs for any errors
sudo journalctl -u lifeadmin-backend.service -n 50 --no-pager
```

Verify the backend started successfully and Stripe is initialized.

## Step 5: Update Frontend Environment Variables

Edit the frontend `.env` file:

```bash
nano /home/lifeadmin/LifeAdmin/frontend/.env
```

Add/update these variables:

```bash
VITE_API_URL=https://remindes.com/api
VITE_STRIPE_PUBLISHABLE_KEY=pk_test_51T0c0A0eEDO9PGJfpRN8BuAPCcDPVg4HY1pbKhMXrmAtIuvfutGHu48RhRzTbJVN4Y30K7P30GpSRV1k8TuWTn0C00OwrgK6Vx
```

Save and exit (Ctrl+X, Y, Enter)

## Step 6: Rebuild and Deploy Frontend

```bash
cd /home/lifeadmin/LifeAdmin/frontend

# Install new dependencies (@stripe/stripe-js)
npm install

# Build production bundle
npm run build

# Verify build completed successfully
ls -lh dist/
```

The dist directory should contain the built frontend files. These should already be served by Nginx.

## Step 7: Set Up Stripe Webhook

1. Log in to Stripe Dashboard: https://dashboard.stripe.com
2. Navigate to **Developers** → **Webhooks**
3. Click **Add endpoint**
4. Configure the endpoint:
   - **Endpoint URL**: `https://remindes.com/api/payments/webhooks/stripe`
   - **Description**: Remindes Production Webhook
   - **Version**: Latest API version
   - **Events to send**: Select these 6 events:
     - `checkout.session.completed`
     - `customer.subscription.created`
     - `customer.subscription.updated`
     - `customer.subscription.deleted`
     - `invoice.payment_succeeded`
     - `invoice.payment_failed`
5. Click **Add endpoint**
6. Copy the **Signing secret** (starts with `whsec_`)
7. Update the backend `.env` file:
   ```bash
   nano /home/lifeadmin/LifeAdmin/backend/.env
   ```
   Add the webhook secret:
   ```bash
   STRIPE_WEBHOOK_SECRET=whsec_your_actual_webhook_secret_here
   ```
8. Restart the backend:
   ```bash
   sudo systemctl restart lifeadmin-backend.service
   ```

## Step 8: Test the Integration

### 8.1 Test Checkout Flow

1. Visit https://remindes.com (while logged in as a test user)
2. Go to the pricing section or subscription page
3. Click "Upgrade to Premium"
4. Use Stripe test card: `4242 4242 4242 4242`
   - Expiry: Any future date
   - CVC: Any 3 digits
   - ZIP: Any 5 digits
5. Complete the checkout
6. Verify redirect to subscription page with success message
7. Check database that user's subscription fields are updated:
   ```bash
   cd /home/lifeadmin/LifeAdmin/backend
   sqlite3 database.db "SELECT id, email, subscription_plan, subscription_status, stripe_customer_id FROM user WHERE email='test@example.com';"
   ```

### 8.2 Test Webhook Events

1. In Stripe Dashboard, go to **Developers** → **Webhooks**
2. Click on your webhook endpoint
3. Check **Recent events** tab
4. Verify all events show "Success" status
5. Check backend logs:
   ```bash
   tail -f /home/lifeadmin/LifeAdmin/backend/app.log | grep -i stripe
   ```

### 8.3 Test Item Limit

1. Log in as a free user (or create a new account)
2. Try to add more than 20 items
3. Verify error message: "Free plan limited to 20 items. Upgrade to Premium for unlimited items."
4. Upgrade to Premium
5. Verify you can now add more than 20 items

### 8.4 Test Customer Portal

1. As a premium user, go to subscription page
2. Click "Manage Subscription"
3. Verify redirect to Stripe Customer Portal
4. Test canceling subscription
5. Verify subscription status updates in database

## Step 9: Monitor and Verify

### Check Backend Logs

```bash
# Watch live logs
tail -f /home/lifeadmin/LifeAdmin/backend/app.log

# Check for Stripe-related events
grep -i stripe /home/lifeadmin/LifeAdmin/backend/app.log | tail -20

# Check for errors
grep -i error /home/lifeadmin/LifeAdmin/backend/app.log | tail -20
```

### Verify Database

```bash
cd /home/lifeadmin/LifeAdmin/backend

# Check user subscription fields
sqlite3 database.db "SELECT id, email, subscription_plan, subscription_status, subscription_current_period_end FROM user LIMIT 10;"

# Count premium users
sqlite3 database.db "SELECT COUNT(*) as premium_users FROM user WHERE subscription_plan='premium' AND subscription_status='active';"
```

### Test All Endpoints

```bash
# Test config endpoint (public)
curl https://remindes.com/api/payments/config

# Test create checkout (requires auth token)
curl -X POST https://remindes.com/api/payments/create-checkout-session \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json"
```

## Troubleshooting

### Issue: Backend won't start after restart

**Solution:**
1. Check logs: `sudo journalctl -u lifeadmin-backend.service -n 50`
2. Verify virtual environment: `source venv/bin/activate && python -c "import stripe; print(stripe.__version__)"`
3. Check .env file has correct Stripe keys
4. Verify database migration completed

### Issue: Webhook signature verification fails

**Solution:**
1. Verify `STRIPE_WEBHOOK_SECRET` is set correctly in `.env`
2. Check webhook URL matches exactly: `https://remindes.com/api/payments/webhooks/stripe`
3. Verify HTTPS is working (Stripe requires HTTPS)
4. Check Stripe Dashboard → Webhooks for error details

### Issue: Checkout session creation fails

**Solution:**
1. Verify `STRIPE_SECRET_KEY` is correct
2. Check `STRIPE_PRICE_ID_PREMIUM` matches your Stripe dashboard
3. Verify `FRONTEND_URL` is set to `https://remindes.com`
4. Check backend logs for detailed error messages

### Issue: Item limit not enforced

**Solution:**
1. Verify migration added subscription columns: `sqlite3 database.db ".schema user"`
2. Check user subscription_plan is set: `sqlite3 database.db "SELECT subscription_plan FROM user;"`
3. Verify backend code changes were deployed
4. Restart backend service

## Rollback Plan

If issues occur and you need to rollback:

```bash
# 1. Revert backend code
cd /home/lifeadmin/LifeAdmin
git checkout main
git pull

# 2. Rebuild frontend
cd frontend
npm install
npm run build

# 3. Restart backend
sudo systemctl restart lifeadmin-backend.service

# Note: Database migration cannot be automatically rolled back
# Subscription columns will remain but won't affect existing functionality
```

## Post-Deployment Checklist

- [ ] Backend service running without errors
- [ ] Frontend displays correctly
- [ ] Stripe checkout flow works
- [ ] Webhooks receiving events (check Stripe Dashboard)
- [ ] User subscriptions updating correctly
- [ ] Item limit enforced for free users
- [ ] Premium users have unlimited items
- [ ] Customer portal accessible
- [ ] Subscription cancellation works
- [ ] All environment variables set correctly
- [ ] Logs monitored for errors
- [ ] Database backup created

## Support and Monitoring

- **Stripe Dashboard**: https://dashboard.stripe.com
- **Backend Logs**: `/home/lifeadmin/LifeAdmin/backend/app.log`
- **Service Status**: `sudo systemctl status lifeadmin-backend.service`
- **Database**: `/home/lifeadmin/LifeAdmin/backend/database.db`

For detailed setup and troubleshooting information, see `STRIPE_SETUP.md` in the repository root.
