import unittest
from app.validators import validate_email, validate_positive_int
from app.errors import ValidationError

class TestValidators(unittest.TestCase):

    def test_validate_email_success(self):
        email = validate_email("TEST@Example.COM ")
        self.assertEqual(email, "test@example.com")

    def test_validate_email_invalid(self):
        with self.assertRaises(ValidationError):
            validate_email("invalid-email")

    def test_validate_positive_int(self):
        validate_positive_int(5, "count")

    def test_validate_positive_int_invalid(self):
        with self.assertRaises(ValidationError):
            validate_positive_int(0, "count")
