
import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class TestSearchByCategory(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
        self.cart.items = [
            DigitalVideoDisc("The Lion King", category="Animation"),
            DigitalVideoDisc("Star Wars", category="Sci-Fi"),
            DigitalVideoDisc("Aladdin", category="Animation"),
        ]

    def test_search_case_insensitive(self):
        results = search_by_category(self.cart, " animation ")

        titles = [dvd.title for dvd in results]

        self.assertEqual(
            titles,
            ["The Lion King", "Aladdin"]
        )

    def test_search_empty_category(self):
        results = search_by_category(self.cart, " ")

        self.assertEqual(results, [])


if __name__ == "__main__":
    unittest.main()
