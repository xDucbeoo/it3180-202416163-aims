
import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCartDiscount(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
        dvd = DigitalVideoDisc(
            "Test DVD",
            "Test",
            cost=100.0
        )
        self.cart.add_dvd(dvd)

    def test_discount_20_percent(self):
        # 100 USD with 20% discount = 80 USD
        result = self.cart.total_cost_with_discount(20)
        self.assertAlmostEqual(result, 80.0)

    def test_discount_zero_percent(self):
        # 0% discount must keep the original cost
        result = self.cart.total_cost_with_discount(0)
        self.assertAlmostEqual(result, 100.0)

    def test_invalid_discount_percent(self):
        # Discount greater than 100% must be rejected
        with self.assertRaises(ValueError):
            self.cart.total_cost_with_discount(150)


if __name__ == "__main__":
    unittest.main()
