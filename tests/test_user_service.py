import unittest
from app.user_service import create_user, get_user
from app.errors import ValidationError

class TestUserService(unittest.TestCase):

    def test_create_and_get_user(self):
        user = create_user("u1", "user@example.com")
        fetched = get_user("u1")

        self.assertEqual(user["id"], fetched["id"])
        self.assertEqual(user["email"], "user@example.com")

    def test_create_user_invalid_email(self):
        with self.assertRaises(ValidationError):
            create_user("u2", "invalid-email")
