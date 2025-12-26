from datetime import datetime

def utc_now_iso() -> str:
    return datetime.utcnow().isoformat()

def normalize_email(email: str) -> str:
    return email.strip().lower()
