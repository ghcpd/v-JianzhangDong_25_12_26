import pytest
from app.errors import AppError, AuthError, ValidationError, RepositoryError


def test_app_error():
    with pytest.raises(AppError):
        raise AppError("Test error")


def test_auth_error():
    with pytest.raises(AuthError):
        raise AuthError("Auth failed")


def test_validation_error():
    with pytest.raises(ValidationError):
        raise ValidationError("Invalid data")


def test_repository_error():
    with pytest.raises(RepositoryError):
        raise RepositoryError("Repo error")