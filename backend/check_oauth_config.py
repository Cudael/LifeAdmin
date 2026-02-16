#!/usr/bin/env python3
"""
OAuth Configuration Checker
Validates that Google OAuth is properly configured for production
"""
import os
from dotenv import load_dotenv

load_dotenv()

def check_oauth_config():
    print("🔍 Checking Google OAuth Configuration...\n")
    
    issues = []
    warnings = []
    
    # Check required variables
    client_id = os.getenv('GOOGLE_CLIENT_ID')
    client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
    redirect_uri = os.getenv('OAUTH_REDIRECT_URI')
    frontend_url = os.getenv('FRONTEND_URL')
    
    if not client_id or client_id == 'your-google-client-id':
        issues.append("❌ GOOGLE_CLIENT_ID is not set or using default value")
    else:
        print(f"✅ GOOGLE_CLIENT_ID: {client_id[:20]}...")
    
    if not client_secret or client_secret == 'your-google-client-secret':
        issues.append("❌ GOOGLE_CLIENT_SECRET is not set or using default value")
    else:
        print(f"✅ GOOGLE_CLIENT_SECRET: {'*' * 20}")
    
    if not redirect_uri:
        warnings.append("⚠️  OAUTH_REDIRECT_URI not set - will use auto-detection")
        print("⚠️  OAUTH_REDIRECT_URI: Not set (auto-detect mode)")
    else:
        print(f"✅ OAUTH_REDIRECT_URI: {redirect_uri}")
        
        # Validate redirect URI format
        if not redirect_uri.startswith('http'):
            issues.append("❌ OAUTH_REDIRECT_URI must start with http:// or https://")
        
        if not redirect_uri.endswith('/auth/google/callback'):
            issues.append("❌ OAUTH_REDIRECT_URI must end with /auth/google/callback")
    
    if not frontend_url:
        issues.append("❌ FRONTEND_URL is not set")
    else:
        print(f"✅ FRONTEND_URL: {frontend_url}")
    
    # Summary
    print("\n" + "="*60)
    if issues:
        print("❌ Configuration Issues Found:\n")
        for issue in issues:
            print(f"  {issue}")
        return False
    elif warnings:
        print("⚠️  Configuration Warnings:\n")
        for warning in warnings:
            print(f"  {warning}")
        print("\n✅ Configuration is functional but has warnings")
        return True
    else:
        print("✅ All OAuth configuration checks passed!")
        return True

if __name__ == "__main__":
    success = check_oauth_config()
    exit(0 if success else 1)
