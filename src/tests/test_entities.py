import unittest
from ..domain import Restrictions
from .mocks import MockGetFilter

class TestEntities(unittest.TestCase):
    def test_get_filer(self):
        expected = MockGetFilter().get_filter()
        response = Restrictions().get_filter()
        self.assertEqual(expected, response)
