import unittest
from datetime import datetime
from app.utils import normalize_email, utc_now_iso


class TestUtils(unittest.TestCase):
    def test_normalize_email(self):
        self.assertEqual(normalize_email("  Foo@Bar.COM \n"), "foo@bar.com")

    def test_utc_now_iso_returns_parseable_timestamp(self):
        ts = utc_now_iso()
        dt = datetime.fromisoformat(ts)
        now = datetime.utcnow()
        # timestamp should be reasonably recent (10 seconds)
        self.assertTrue(abs((now - dt).total_seconds()) < 10)
