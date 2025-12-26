import unittest
from app.discount import apply_discount


class TestDiscount(unittest.TestCase):
    def test_vip_discount(self):
        self.assertEqual(apply_discount(100.0, "vip"), 80.0)

    def test_staff_discount(self):
        self.assertEqual(apply_discount(200.0, "staff"), 100.0)

    def test_no_discount(self):
        self.assertEqual(apply_discount(50.0, "regular"), 50.0)
