class AppError(Exception):
    """Base class for application errors."""


class AuthError(AppError):
    pass


class ValidationError(AppError):
    pass


class RepositoryError(AppError):
    pass
