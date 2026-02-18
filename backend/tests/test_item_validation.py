import pytest
from fastapi import HTTPException
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from utils.item_validation import validate_item_fields

def test_valid_item_passes():
    validate_item_fields("My Passport", "document", "Travel")  # should not raise

def test_empty_name_raises():
    with pytest.raises(HTTPException) as exc:
        validate_item_fields("  ", "document", "Travel")
    assert exc.value.status_code == 422

def test_invalid_type_raises():
    with pytest.raises(HTTPException) as exc:
        validate_item_fields("My Item", "invoice", "Travel")
    assert exc.value.status_code == 422

def test_invalid_category_raises():
    with pytest.raises(HTTPException) as exc:
        validate_item_fields("My Item", "document", "Unknown")
    assert exc.value.status_code == 422

def test_valid_subscription_passes():
    validate_item_fields("Netflix", "subscription", "Subscriptions")
