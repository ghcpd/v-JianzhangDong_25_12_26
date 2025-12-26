import unittest
from app.pricing import calculate_price

class TestPricing(unittest.TestCase):

    def test_vip_discount(self):
        self.assertEqual(calculate_price(100, "vip"), 80.0)

    def test_staff_discount(self):
        self.assertEqual(calculate_price(100, "staff"), 50.0)

    def test_no_discount(self):
        self.assertEqual(calculate_price(100, "normal"), 100.0)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_price(-1, "vip")
