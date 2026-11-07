
import unittest
from types import SimpleNamespace

from aims.cart import Cart


class TestCartSorting(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
        self.cart.items = [
            SimpleNamespace(title="Star Wars", cost=24.95),
            SimpleNamespace(title="aladdin", cost=18.99),
            SimpleNamespace(title="The Lion King", cost=19.95),
        ]

    def test_sort_by_title(self):
        self.cart.sort_by_title()

        titles = [dvd.title for dvd in self.cart.items]

        self.assertEqual(
            titles,
            ["aladdin", "Star Wars", "The Lion King"]
        )

    def test_sort_by_cost(self):
        total_before = self.cart.total_cost()

        self.cart.sort_by_cost()

        titles = [dvd.title for dvd in self.cart.items]

        self.assertEqual(
            titles,
            ["aladdin", "The Lion King", "Star Wars"]
        )

        self.assertAlmostEqual(
            self.cart.total_cost(),
            total_before
        )


if __name__ == "__main__":
    unittest.main()
