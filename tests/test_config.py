import unittest
import os
from app import config

class TestConfig(unittest.TestCase):

    def test_default_env(self):
        if "APP_ENV" in os.environ:
            del os.environ["APP_ENV"]
        self.assertEqual(config.get_env(), "development")

    def test_is_production(self):
        os.environ["APP_ENV"] = "production"
        self.assertTrue(config.is_production())
