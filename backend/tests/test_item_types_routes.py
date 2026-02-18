"""
Test item-types routes to ensure no redirects occur.

This test ensures that both /item-types and /item-types/ work without
FastAPI redirecting one to the other, which would cause issues with Nginx.
"""
from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from main import app

client = TestClient(app, follow_redirects=False)


def test_item_types_no_trailing_slash():
    """Test /item-types without trailing slash returns 401 (auth required), not 307 redirect"""
    response = client.get("/item-types")
    # Should be 401 (unauthorized) not 307 (redirect)
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"


def test_item_types_with_trailing_slash():
    """Test /item-types/ with trailing slash returns 401 (auth required), not 307 redirect"""
    response = client.get("/item-types/")
    # Should be 401 (unauthorized) not 307 (redirect)
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"


def test_item_types_categories_no_trailing_slash():
    """Test /item-types/categories without trailing slash returns 401, not 307 redirect"""
    response = client.get("/item-types/categories")
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"


def test_item_types_categories_with_trailing_slash():
    """Test /item-types/categories/ with trailing slash returns 401, not 307 redirect"""
    response = client.get("/item-types/categories/")
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"


def test_item_types_by_id_no_trailing_slash():
    """Test /item-types/1 without trailing slash returns 401, not 307 redirect"""
    response = client.get("/item-types/1")
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"


def test_item_types_by_id_with_trailing_slash():
    """Test /item-types/1/ with trailing slash returns 401, not 307 redirect"""
    response = client.get("/item-types/1/")
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"
