import pytest
import os

# Use in-memory SQLite for tests
os.environ["DATABASE_URL"] = "sqlite://"
