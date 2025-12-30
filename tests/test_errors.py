import unittest
from app.errors import AppError, AuthError, ValidationError, RepositoryError


class TestErrors(unittest.TestCase):

    def test_app_error_is_exception(self):
        """Test that AppError is an Exception"""
        error = AppError("test error")
        self.assertIsInstance(error, Exception)

    def test_app_error_message(self):
        """Test AppError message"""
        message = "test error message"
        error = AppError(message)
        self.assertEqual(str(error), message)

    def test_auth_error_is_app_error(self):
        """Test that AuthError is an AppError"""
        error = AuthError("auth failed")
        self.assertIsInstance(error, AppError)

    def test_auth_error_is_exception(self):
        """Test that AuthError is an Exception"""
        error = AuthError("auth failed")
        self.assertIsInstance(error, Exception)

    def test_auth_error_message(self):
        """Test AuthError message"""
        message = "authentication failed"
        error = AuthError(message)
        self.assertEqual(str(error), message)

    def test_validation_error_is_app_error(self):
        """Test that ValidationError is an AppError"""
        error = ValidationError("invalid input")
        self.assertIsInstance(error, AppError)

    def test_validation_error_is_exception(self):
        """Test that ValidationError is an Exception"""
        error = ValidationError("invalid input")
        self.assertIsInstance(error, Exception)

    def test_validation_error_message(self):
        """Test ValidationError message"""
        message = "field is required"
        error = ValidationError(message)
        self.assertEqual(str(error), message)

    def test_repository_error_is_app_error(self):
        """Test that RepositoryError is an AppError"""
        error = RepositoryError("database error")
        self.assertIsInstance(error, AppError)

    def test_repository_error_is_exception(self):
        """Test that RepositoryError is an Exception"""
        error = RepositoryError("database error")
        self.assertIsInstance(error, Exception)

    def test_repository_error_message(self):
        """Test RepositoryError message"""
        message = "failed to connect to database"
        error = RepositoryError(message)
        self.assertEqual(str(error), message)

    def test_error_raising(self):
        """Test raising and catching errors"""
        with self.assertRaises(AppError):
            raise AppError("test")

    def test_auth_error_raising(self):
        """Test raising and catching AuthError"""
        with self.assertRaises(AuthError):
            raise AuthError("unauthorized")

    def test_validation_error_raising(self):
        """Test raising and catching ValidationError"""
        with self.assertRaises(ValidationError):
            raise ValidationError("invalid")

    def test_repository_error_raising(self):
        """Test raising and catching RepositoryError"""
        with self.assertRaises(RepositoryError):
            raise RepositoryError("repository failure")


if __name__ == "__main__":
    unittest.main()
