import unittest
from datetime import datetime
from app.utils import normalize_email, utc_now_iso


class TestUtils(unittest.TestCase):

    def test_normalize_email(self):
        self.assertEqual(normalize_email(" TEST@Example.COM "), "test@example.com")

    def test_utc_now_iso_parsable(self):
        val = utc_now_iso()
        # should be ISO-parseable and produce a naive UTC datetime
        parsed = datetime.fromisoformat(val)
        self.assertIsInstance(parsed, datetime)
