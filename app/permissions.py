def has_permission(role: str, action: str) -> bool:
    if role == "admin":
        return True
    if role == "user" and action in {"read"}:
        return True
    return False
