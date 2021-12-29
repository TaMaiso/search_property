import unittest
from .mocks import MockController
from ..deal import Controller

class TestController(unittest.TestCase):
    def setUp(self):
        self.resolve = {'year': ['2011'], 'city': ['Bogota'], 'price': ['3000000']}

    def test_get_params_property(self):
        expected = MockController(self.resolve).get_params()
        result = Controller(self.resolve).get_params()
        self.assertEqual(result, expected)

