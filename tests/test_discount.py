import unittest
from app.discount import apply_discount


class TestDiscount(unittest.TestCase):

    def test_apply_discount_vip(self):
        """Test VIP discount (20% off - price * 0.8)"""
        result = apply_discount(100.0, "vip")
        self.assertEqual(result, 80.0)

    def test_apply_discount_vip_decimal(self):
        """Test VIP discount with decimal prices"""
        result = apply_discount(50.50, "vip")
        self.assertAlmostEqual(result, 40.4, places=2)

    def test_apply_discount_staff(self):
        """Test staff discount (50% off - price * 0.5)"""
        result = apply_discount(100.0, "staff")
        self.assertEqual(result, 50.0)

    def test_apply_discount_staff_decimal(self):
        """Test staff discount with decimal prices"""
        result = apply_discount(99.99, "staff")
        self.assertAlmostEqual(result, 49.995, places=2)

    def test_apply_discount_regular_user(self):
        """Test no discount for regular user"""
        result = apply_discount(100.0, "regular")
        self.assertEqual(result, 100.0)

    def test_apply_discount_no_level(self):
        """Test no discount when user level is unknown"""
        result = apply_discount(100.0, "guest")
        self.assertEqual(result, 100.0)

    def test_apply_discount_zero_price(self):
        """Test discount on zero price"""
        result = apply_discount(0.0, "vip")
        self.assertEqual(result, 0.0)

    def test_apply_discount_large_price(self):
        """Test discount on large prices"""
        result = apply_discount(10000.0, "staff")
        self.assertEqual(result, 5000.0)


if __name__ == "__main__":
    unittest.main()
