import unittest
from app.repository import InMemoryRepository
from app.errors import RepositoryError

class TestRepository(unittest.TestCase):

    def test_save_and_get(self):
        repo = InMemoryRepository()
        repo.save("k1", {"value": 123})
        self.assertEqual(repo.get("k1")["value"], 123)

    def test_get_missing_key(self):
        repo = InMemoryRepository()
        with self.assertRaises(RepositoryError):
            repo.get("missing")
