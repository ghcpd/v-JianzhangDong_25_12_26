import unittest
from app.auth import authenticate
from app.errors import AuthError

class TestAuth(unittest.TestCase):

    def test_valid_token(self):
        self.assertTrue(authenticate("valid-token-123"))

    def test_invalid_token(self):
        self.assertFalse(authenticate("invalid-token"))

    def test_missing_token(self):
        with self.assertRaises(AuthError):
            authenticate("")
