from datetime import datetime, timedelta

from app.utils import normalize_email, utc_now_iso


def test_normalize_email():
    assert normalize_email("  Alice@Example.COM \n") == "alice@example.com"


def test_utc_now_iso_returns_parsable_recent_time():
    s = utc_now_iso()
    # should be ISO-parsable and within a few seconds of now
    dt = datetime.fromisoformat(s)
    assert datetime.utcnow() - dt < timedelta(seconds=10)
