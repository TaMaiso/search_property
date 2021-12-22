import unittest
from .mocks import MockGetParamsProperty
from ..deal import get_params_property

class TestHandler(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_params_property(self):
        mock = MockGetParamsProperty('2011', 'Bogota', '3000000')
        resolve =  mock.get_request()
        result = get_params_property(resolve)
        expect = mock.get_resolve()
        self.assertEqual(result, expect)

