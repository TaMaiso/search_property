import unittest
from ..data import Handler, Codes, Status, Msgs, Env
from .mocks import MockMakeResponse, MockFindMethodAndHandler

mock_config = {
    'HOST': "sdfgas",
    'PORT': "sdfgas",
    'USER': "sdfgas",
    'PASSWORD': "sdfgas",
    'DATABASE': "sdfgas"
}


class TestHandler(unittest.TestCase):
    def setUp(self):
        self.app = Handler()

    def test_find_method_path_get(self):
        mock_find_method_path= MockFindMethodAndHandler(Env, "get", "/hello")
        env = mock_find_method_path.get_env()
        mock_response = mock_find_method_path.get_response()
        response = self.app.find_method_path(env)
        self.assertEqual(response, mock_response)

    def test_find_method_path_post(self):
        mock_find_method_path= MockFindMethodAndHandler(Env, "post", "/hi")
        env = mock_find_method_path.get_env()
        mock_response = mock_find_method_path.get_response()
        response = self.app.find_method_path(env)
        self.assertEqual(response, mock_response)


    def test_find_status_body_handler(self):
        pass

    def test_make_response_generics(self):
        mock_make_response = MockMakeResponse("a","b","c","d")
        code, msg, status, data = mock_make_response.get_params()
        mock_response = mock_make_response.get_response()
        response  = self.app.make_response(code, msg, status, data)
        self.assertEqual(response, mock_response)

    def test_make_response_success(self):
        mock_make_response = MockMakeResponse(
            Codes['OK'].value, 
            Msgs['OK'].value, 
            {"with":"data"}, 
            Status['SUCCESS'].value
        )
        code, msg, status, data = mock_make_response.get_params()
        mock_response = mock_make_response.get_response()
        response  = self.app.make_response(code, msg, status, data)
        self.assertEqual(response, mock_response)

    def test_make_response_fail(self):
        mock_make_response = MockMakeResponse(
            Codes['NOT_FOUND'].value, 
            Msgs['NOT_FOUND'].value, 
            None, 
            Status['FAIL'].value
        )
        code, msg, status, data = mock_make_response.get_params()
        mock_response = mock_make_response.get_response()
        response  = self.app.make_response(code, msg, status, data)
        self.assertEqual(response, mock_response)

if __name__=='__main__':
    unittest.main()