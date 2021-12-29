import unittest
from ..domain import PropRestrictions, PropFilters
from .mocks import MockEntities

class TestEntities(unittest.TestCase):
    def setUp(self):
        self.year = "2201"
        self.price = "300000000"
        self.city = "bogota"

    def test_get_filters_by_nothing(self):
        expected = MockEntities().get_filters()
        response = PropFilters().get_filters()
        self.assertEqual(response, expected)

    def test_get_filters_by_year(self):
        expected = MockEntities(self.year).get_filters()
        response = PropFilters(self.year).get_filters()
        self.assertEqual(response, expected)

    def test_get_filters_by_price(self):
        expected = MockEntities(self.price).get_filters()
        response = PropFilters(self.price).get_filters()
        self.assertEqual(response, expected)

    def test_get_filters_by_city(self):
        expected = MockEntities(self.city).get_filters()
        response = PropFilters(self.city).get_filters()
        self.assertEqual(response, expected)

    def test_get_filters_by_year_city(self):
        expected = MockEntities(self.year, self.city).get_filters()
        response = PropFilters(self.year, self.city).get_filters()
        self.assertEqual(response, expected)

    def test_get_filters_by_year_price(self):
        expected = MockEntities(year=self.year, price=self.price).get_filters()
        response = PropFilters(year=self.year, price=self.price).get_filters()
        self.assertEqual(response, expected)

    def test_get_filters_by_city_price(self):
        expected = MockEntities(city=self.city, price=self.price).get_filters()
        response = PropFilters(city=self.city, price=self.price).get_filters()
        self.assertEqual(response, expected)

    def test_get_filters_by_year_city_price(self):
        expected = MockEntities(self.year, self.city, self.price).get_filters()
        response = PropFilters(self.year, self.city, self.price).get_filters()
        self.assertEqual(response, expected)

    def test_get_filter(self):
        expected = MockEntities().get_restrictions()
        response = PropRestrictions().get_filter()
        self.assertEqual(expected, response)
