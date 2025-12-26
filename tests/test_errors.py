import unittest
from app.errors import AppError, AuthError, ValidationError, RepositoryError


class TestErrors(unittest.TestCase):
    def test_error_hierarchy(self):
        self.assertTrue(issubclass(AuthError, AppError))
        self.assertTrue(issubclass(ValidationError, AppError))
        self.assertTrue(issubclass(RepositoryError, AppError))
        self.assertTrue(issubclass(AppError, Exception))

    def test_can_raise_specific_errors(self):
        with self.assertRaises(AuthError):
            raise AuthError("auth failed")
        with self.assertRaises(ValidationError):
            raise ValidationError("validation failed")
        with self.assertRaises(RepositoryError):
            raise RepositoryError("repo failed")
