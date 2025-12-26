from app.errors import ValidationError
from app.utils import normalize_email

def validate_email(email: str) -> str:
    email = normalize_email(email)
    if "@" not in email:
        raise ValidationError("Invalid email address")
    return email

def validate_positive_int(value: int, field: str) -> None:
    if value <= 0:
        raise ValidationError(f"{field} must be positive")
