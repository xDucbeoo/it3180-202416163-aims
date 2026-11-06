
import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):

    def test_add_dvd_until_full(self):
        cart = Cart()

        # Add the first 20 DVDs.
        for i in range(MAX_NUMBERS_ORDERED):
            dvd = DigitalVideoDisc(
                f"DVD {i + 1}",
                "Test",
                cost=10.0
            )
            self.assertTrue(cart.add_dvd(dvd))

        # The 21st DVD must be rejected.
        extra_dvd = DigitalVideoDisc(
            "DVD 21",
            "Test",
            cost=10.0
        )

        self.assertFalse(cart.add_dvd(extra_dvd))

        # The cart must contain exactly 20 DVDs.
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)


if __name__ == "__main__":
    unittest.main()
    