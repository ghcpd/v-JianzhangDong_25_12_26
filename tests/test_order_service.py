import unittest
from app.order_service import create_order, get_order
from app.errors import ValidationError

class TestOrderService(unittest.TestCase):

    def test_create_and_get_order(self):
        order = create_order("o1", 100, "vip")
        self.assertEqual(order["price"], 80.0)

        fetched = get_order("o1")
        self.assertEqual(fetched["status"], "created")

    def test_create_order_invalid_price(self):
        with self.assertRaises(ValidationError):
            create_order("o2", 0, "normal")
