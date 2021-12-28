import unittest
from .mocks import MockRepository
from ..deal import Repository

class TestHandler(unittest.TestCase):
    def setUp(self):
        self.year = "2201"
        self.price = "300000000"
        self.city = "bogota"
        self.maxDiff = None

    def test_get_filters_by_nothing(self):
        expected = MockRepository().get_filters()
        response = Repository().get_filters()
        self.assertEqual(response, expected)

    def test_get_filters_by_year(self):
        expected = MockRepository(self.year).get_filters()
        response = Repository(self.year).get_filters()
        self.assertEqual(response, expected)

    def test_get_filters_by_price(self):
        expected = MockRepository(self.price).get_filters()
        response = Repository(self.price).get_filters()
        self.assertEqual(response, expected)

    def test_get_filters_by_city(self):
        expected = MockRepository(self.city).get_filters()
        response = Repository(self.city).get_filters()
        self.assertEqual(response, expected)

    def test_get_filters_by_year_city(self):
        expected = MockRepository(self.year, self.city).get_filters()
        response = Repository(self.year, self.city).get_filters()
        self.assertEqual(response, expected)

    def test_get_filters_by_year_price(self):
        expected = MockRepository(year=self.year, price=self.price).get_filters()
        response = Repository(year=self.year, price=self.price).get_filters()
        self.assertEqual(response, expected)

    def test_get_filters_by_city_price(self):
        expected = MockRepository(city=self.city, price=self.price).get_filters()
        response = Repository(city=self.city, price=self.price).get_filters()
        self.assertEqual(response, expected)

    def test_get_filters_by_year_city_price(self):
        expected = MockRepository(self.year, self.city, self.price).get_filters()
        response = Repository(self.year, self.city, self.price).get_filters()
        self.assertEqual(response, expected)
    
    def test_get_query(self):
        expected = """\
            SELECT property.id, property.address, property.city, property.price, property.description, status.name AS status\
            FROM habi_db.status_history AS history\
            INNER JOIN (\
                SELECT sh.property_id AS id, MAX(sh.update_date) AS date\
                FROM habi_db.status_history AS sh\
                WHERE sh.status_id = 3 OR sh.status_id = 4 OR sh.status_id = 5\
                GROUP BY sh.property_id)\
            AS sh ON (\
                sh.id = history.property_id and sh.date = history.update_date)\
            INNER JOIN habi_db.property AS property\
            ON property.id = history.property_id\
            INNER JOIN habi_db.status AS status\
            ON status.id  = history.status_id\
            WHERE property.year = {} AND property.city = '{}' AND property.price > {}\
        """.format(self.year, self.city, self.price)
        response = Repository(self.year, self.city, self.price).get_query()
        self.assertEqual(response, expected)