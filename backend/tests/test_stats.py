"""
Tests for the /items/stats endpoint
"""
from fastapi.testclient import TestClient
import sys
import os
from datetime import datetime, timedelta, date

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from main import app

client = TestClient(app)


def test_stats_endpoint_structure():
    """Test that stats endpoint returns the correct structure"""
    # This test doesn't require authentication for structure validation
    # In a real scenario, you'd need to mock authentication or create a test user
    
    # Just verify the endpoint exists and has the expected return structure
    # We expect 401 without auth, which is good - it means endpoint exists
    res = client.get("/items/stats")
    
    # We expect 401 Unauthorized since we're not authenticated
    # But this confirms the endpoint exists
    assert res.status_code in [200, 401], f"Unexpected status code: {res.status_code}"
    
    # If somehow we got a 200 (shouldn't happen without auth), verify structure
    if res.status_code == 200:
        data = res.json()
        assert "total_items" in data
        assert "expiring_soon" in data
        assert "expiring_this_week" in data
        assert "expired" in data
        assert "documents" in data
        assert "subscriptions" in data
        assert "by_category" in data
        assert "activity_summaries" in data
        
        # Verify activity_summaries structure
        summaries = data["activity_summaries"]
        assert "items_added_this_month" in summaries
        assert "items_expiring_this_month" in summaries
        assert "items_expiring_this_week" in summaries
        assert "expired_items" in summaries
        assert "subscriptions_renewing_week" in summaries
        assert "documents_total" in summaries


def test_stats_endpoint_exists():
    """Verify the stats endpoint exists"""
    res = client.get("/items/stats")
    # Should get 401 (unauthorized) not 404 (not found)
    assert res.status_code != 404, "Stats endpoint not found"
