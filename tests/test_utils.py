import pytest
from app.utils import utc_now_iso, normalize_email


def test_utc_now_iso():
    result = utc_now_iso()
    assert isinstance(result, str)
    # Check if it looks like ISO format
    assert "T" in result


def test_normalize_email():
    assert normalize_email("  Test@Example.COM  ") == "test@example.com"
    assert normalize_email("user@domain.org") == "user@domain.org"