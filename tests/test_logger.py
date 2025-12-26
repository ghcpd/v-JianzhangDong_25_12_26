import unittest
from app.logger import get_logger

class TestLogger(unittest.TestCase):

    def test_get_logger_returns_instance(self):
        logger = get_logger()
        self.assertIsNotNone(logger)

    def test_get_logger_same_instance(self):
        logger1 = get_logger()
        logger2 = get_logger()
        self.assertIs(logger1, logger2)
