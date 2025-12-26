import unittest
from unittest.mock import patch
from datetime import datetime
from app.utils import utc_now_iso, normalize_email


class TestUtilsUtcNow(unittest.TestCase):

    def test_utc_now_iso_returns_string(self):
        """Test that utc_now_iso returns a string"""
        result = utc_now_iso()
        self.assertIsInstance(result, str)

    def test_utc_now_iso_is_valid_iso_format(self):
        """Test that utc_now_iso returns valid ISO format"""
        result = utc_now_iso()
        # Should be parseable as ISO format
        try:
            datetime.fromisoformat(result)
        except ValueError:
            self.fail("utc_now_iso() did not return valid ISO format")

    def test_utc_now_iso_contains_t(self):
        """Test that ISO format contains 'T' separator"""
        result = utc_now_iso()
        self.assertIn("T", result)

    @patch("app.utils.datetime")
    def test_utc_now_iso_uses_utcnow(self, mock_datetime):
        """Test that utc_now_iso uses utcnow"""
        mock_datetime.utcnow.return_value = datetime(2025, 12, 26, 10, 30, 45, 123456)
        result = utc_now_iso()
        mock_datetime.utcnow.assert_called_once()

    def test_utc_now_iso_approximate_timestamp(self):
        """Test that utc_now_iso returns a recent timestamp"""
        result = utc_now_iso()
        now = datetime.utcnow()
        # Parse the ISO format and check it's close to current time
        parsed = datetime.fromisoformat(result)
        # Should be within 1 second
        delta = abs((now - parsed).total_seconds())
        self.assertLess(delta, 2)


class TestNormalizeEmail(unittest.TestCase):

    def test_normalize_email_lowercase(self):
        """Test email is converted to lowercase"""
        result = normalize_email("TEST@EXAMPLE.COM")
        self.assertEqual(result, "test@example.com")

    def test_normalize_email_mixed_case(self):
        """Test mixed case email normalization"""
        result = normalize_email("John.Doe@Example.COM")
        self.assertEqual(result, "john.doe@example.com")

    def test_normalize_email_strips_whitespace(self):
        """Test whitespace is stripped"""
        result = normalize_email("  test@example.com  ")
        self.assertEqual(result, "test@example.com")

    def test_normalize_email_strips_and_lowercase(self):
        """Test both stripping and lowercase"""
        result = normalize_email("  TEST@EXAMPLE.COM  ")
        self.assertEqual(result, "test@example.com")

    def test_normalize_email_leading_whitespace(self):
        """Test leading whitespace is stripped"""
        result = normalize_email("  user@domain.com")
        self.assertEqual(result, "user@domain.com")

    def test_normalize_email_trailing_whitespace(self):
        """Test trailing whitespace is stripped"""
        result = normalize_email("user@domain.com  ")
        self.assertEqual(result, "user@domain.com")

    def test_normalize_email_tabs_and_newlines(self):
        """Test tabs and newlines are stripped"""
        result = normalize_email("\t\ntest@example.com\n\t")
        self.assertEqual(result, "test@example.com")

    def test_normalize_email_with_plus_sign(self):
        """Test email with plus sign (Gmail-style)"""
        result = normalize_email("USER+TAG@EXAMPLE.COM")
        self.assertEqual(result, "user+tag@example.com")

    def test_normalize_email_already_normalized(self):
        """Test email that's already normalized"""
        email = "user@example.com"
        result = normalize_email(email)
        self.assertEqual(result, email)

    def test_normalize_email_subdomain(self):
        """Test email with subdomain"""
        result = normalize_email("USER@MAIL.EXAMPLE.COM")
        self.assertEqual(result, "user@mail.example.com")

    def test_normalize_email_numeric(self):
        """Test email with numbers"""
        result = normalize_email("USER123@EXAMPLE.COM")
        self.assertEqual(result, "user123@example.com")

    def test_normalize_email_special_characters(self):
        """Test email with allowed special characters"""
        result = normalize_email("USER.NAME+TAG@EXAMPLE.COM")
        self.assertEqual(result, "user.name+tag@example.com")


if __name__ == "__main__":
    unittest.main()
