import os

DEFAULT_ENV = "development"

def get_env() -> str:
    return os.getenv("APP_ENV", DEFAULT_ENV)

def is_production() -> bool:
    return get_env() == "production"

def database_url() -> str:
    return os.getenv("DATABASE_URL", "sqlite:///:memory:")
