import unittest
from app.discount import apply_discount


class TestDiscount(unittest.TestCase):

    def test_vip_discount(self):
        self.assertAlmostEqual(apply_discount(100.0, "vip"), 80.0)

    def test_staff_discount(self):
        self.assertAlmostEqual(apply_discount(100.0, "staff"), 50.0)

    def test_no_discount(self):
        self.assertAlmostEqual(apply_discount(100.0, "regular"), 100.0)

    def test_zero_and_negative_price(self):
        self.assertAlmostEqual(apply_discount(0.0, "vip"), 0.0)
        # behavior: negative price is passed through the same multiplier
        self.assertAlmostEqual(apply_discount(-10.0, "staff"), -5.0)
