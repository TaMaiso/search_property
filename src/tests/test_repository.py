import unittest
from .mocks import MockGetFilters
from ..deal import Repository

class TestHandler(unittest.TestCase):
    def setUp(self):
        self.year = "2201"
        self.price = "300000000"
        self.city = "bogota"

    def test_get_filters_by_nothing(self):
        expected = MockGetFilters().get_filters()
        response = Repository().get_filters()
        self.assertEqual(response, expected)

    def test_get_filters_by_year(self):
        expected = MockGetFilters(self.year).get_filters()
        response = Repository(self.year).get_filters()
        self.assertEqual(response, expected)

    def test_get_filters_by_price(self):
        expected = MockGetFilters(self.price).get_filters()
        response = Repository(self.price).get_filters()
        self.assertEqual(response, expected)

    def test_get_filters_by_city(self):
        expected = MockGetFilters(self.city).get_filters()
        response = Repository(self.city).get_filters()
        self.assertEqual(response, expected)

    def test_get_filters_by_year_city(self):
        expected = MockGetFilters(self.year, self.city).get_filters()
        response = Repository(self.year, self.city).get_filters()
        self.assertEqual(response, expected)

    def test_get_filters_by_year_price(self):
        expected = MockGetFilters(year=self.year, price=self.price).get_filters()
        response = Repository(year=self.year, price=self.price).get_filters()
        self.assertEqual(response, expected)

    def test_get_filters_by_city_price(self):
        expected = MockGetFilters(city=self.city, price=self.price).get_filters()
        response = Repository(city=self.city, price=self.price).get_filters()
        self.assertEqual(response, expected)

    def test_get_filters_by_year_city_price(self):
        expected = MockGetFilters(self.year, self.city, self.price).get_filters()
        response = Repository(self.year, self.city, self.price).get_filters()
        self.assertEqual(response, expected)