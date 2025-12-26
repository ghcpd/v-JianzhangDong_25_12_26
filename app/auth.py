from app.errors import AuthError

def authenticate(token: str) -> bool:
    if not token:
        raise AuthError("Missing authentication token")
    return token.startswith("valid-")
