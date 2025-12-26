from app.errors import RepositoryError

class InMemoryRepository:
    def __init__(self):
        self._data = {}

    def save(self, key: str, value: dict) -> None:
        if not key:
            raise RepositoryError("Key cannot be empty")
        self._data[key] = value

    def get(self, key: str) -> dict:
        try:
            return self._data[key]
        except KeyError:
            raise RepositoryError(f"Key not found: {key}")
