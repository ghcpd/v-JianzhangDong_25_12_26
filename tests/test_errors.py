import unittest
from app.errors import AppError, AuthError, ValidationError, RepositoryError


class TestErrors(unittest.TestCase):

    def test_subclassing(self):
        self.assertTrue(issubclass(AuthError, AppError))
        self.assertTrue(issubclass(ValidationError, AppError))
        self.assertTrue(issubclass(RepositoryError, AppError))

    def test_raise_and_catch(self):
        with self.assertRaises(ValidationError):
            raise ValidationError("invalid")

    def test_str_message(self):
        e = RepositoryError("repo failed")
        self.assertEqual(str(e), "repo failed")
