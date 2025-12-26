from app.validators import validate_email
from app.repository import InMemoryRepository

_repo = InMemoryRepository()

def create_user(user_id: str, email: str) -> dict:
    email = validate_email(email)
    user = {
        "id": user_id,
        "email": email,
        "role": "user",
    }
    _repo.save(user_id, user)
    return user

def get_user(user_id: str) -> dict:
    return _repo.get(user_id)
