import unittest
from ..data import Handler

mock_config = {
    'HOST': "sdfgas",
    'PORT': "sdfgas",
    'USER': "sdfgas",
    'PASSWORD': "sdfgas",
    'DATABASE': "sdfgas"
}

class TestHandler(unittest.TestCase):
    def setUp(self):
        self.App = Handler(mock_config)

    def test_handler_default(self):
        result = self.App._handler_default(lambda: {}, **{})
        self.assertEqual(result, '{"data": "not found"}')

if __name__=='__main__':
    unittest.main()