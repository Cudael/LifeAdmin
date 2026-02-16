#!/bin/bash
# nginx-check.sh - Verify Nginx configuration for OAuth routing
# 
# This script checks that your Nginx configuration correctly routes
# OAuth requests to the backend instead of serving them from the frontend.

set -e  # Exit on error

echo "🔍 Checking Nginx Configuration for OAuth..."
echo ""

# Check if Nginx is installed
if ! command -v nginx &> /dev/null; then
    echo "❌ Nginx is not installed"
    echo "   Install it with: sudo apt install nginx"
    exit 1
fi

echo "✅ Nginx is installed ($(nginx -v 2>&1 | cut -d'/' -f2))"

# Find the configuration file
CONFIG_FILE=""
POSSIBLE_CONFIGS=(
    "/etc/nginx/sites-available/remindes.com"
    "/etc/nginx/sites-available/default"
    "/etc/nginx/nginx.conf"
    "/etc/nginx/conf.d/default.conf"
)

for config in "${POSSIBLE_CONFIGS[@]}"; do
    if [ -f "$config" ]; then
        CONFIG_FILE="$config"
        break
    fi
done

if [ -z "$CONFIG_FILE" ]; then
    echo "⚠️  Could not find Nginx configuration file"
    echo "   Checked: ${POSSIBLE_CONFIGS[*]}"
    echo "   Please specify your config file manually"
    exit 1
fi

echo "📄 Using config: $CONFIG_FILE"
echo ""

# Check for auth proxy configuration
echo "Checking /auth/ proxy configuration..."
if grep -q "location /auth/" "$CONFIG_FILE"; then
    echo "✅ Found 'location /auth/' proxy configuration"
    
    # Show the configuration
    echo ""
    echo "Configuration block:"
    echo "---"
    grep -A 8 "location /auth/" "$CONFIG_FILE" | head -9 | sed 's/^/   /'
    echo "---"
    echo ""
else
    echo "❌ No 'location /auth/' proxy configuration found!"
    echo ""
    echo "   ⚠️  OAuth callbacks will NOT work without this!"
    echo ""
    echo "   Add this to your Nginx config BEFORE the 'location /' block:"
    echo ""
    echo "   location /auth/ {"
    echo "       proxy_pass http://localhost:8000/auth/;"
    echo "       proxy_set_header Host \$host;"
    echo "       proxy_set_header X-Real-IP \$remote_addr;"
    echo "       proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;"
    echo "       proxy_set_header X-Forwarded-Proto \$scheme;"
    echo "       proxy_set_header X-Forwarded-Host \$host;"
    echo "       proxy_redirect off;"
    echo "   }"
    echo ""
    exit 1
fi

# Check location block order
echo "Checking location block order..."
echo ""

# Extract line numbers for location blocks
AUTH_LINE=$(grep -n "location /auth/" "$CONFIG_FILE" | head -1 | cut -d':' -f1)
ROOT_LINE=$(grep -n "location / {" "$CONFIG_FILE" | head -1 | cut -d':' -f1)

if [ -n "$AUTH_LINE" ] && [ -n "$ROOT_LINE" ]; then
    if [ "$AUTH_LINE" -lt "$ROOT_LINE" ]; then
        echo "✅ Location blocks are in correct order:"
        echo "   - /auth/ at line $AUTH_LINE (proxies to backend)"
        echo "   - /     at line $ROOT_LINE (serves frontend)"
    else
        echo "⚠️  WARNING: Location block order may be incorrect!"
        echo "   - /     at line $ROOT_LINE"
        echo "   - /auth/ at line $AUTH_LINE"
        echo ""
        echo "   The 'location /auth/' block should come BEFORE 'location /'"
        echo "   Otherwise, the frontend will handle OAuth callbacks instead of the backend."
        echo ""
    fi
else
    echo "⚠️  Could not determine location block order"
fi

echo ""

# Check API proxy configuration
echo "Checking /api/ proxy configuration..."
if grep -q "location /api/" "$CONFIG_FILE"; then
    echo "✅ Found 'location /api/' proxy configuration"
else
    echo "⚠️  No 'location /api/' proxy configuration found"
    echo "   API requests may not be proxied to backend correctly"
fi

echo ""

# Test Nginx configuration syntax
echo "Testing Nginx configuration syntax..."
if sudo nginx -t 2>&1 | grep -q "syntax is ok"; then
    echo "✅ Nginx configuration syntax is valid"
else
    echo "❌ Nginx configuration has syntax errors:"
    sudo nginx -t 2>&1 | grep -v "test failed" | sed 's/^/   /'
    exit 1
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Configuration check complete!"
echo ""
echo "🔧 To apply changes after editing config:"
echo "   sudo nginx -t          # Test configuration"
echo "   sudo systemctl reload nginx   # Apply changes"
echo ""
echo "📝 To view full config:"
echo "   cat $CONFIG_FILE"
echo ""
echo "🐛 To debug OAuth issues, check logs:"
echo "   sudo tail -f /var/log/nginx/access.log"
echo "   sudo tail -f /var/log/nginx/error.log"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
