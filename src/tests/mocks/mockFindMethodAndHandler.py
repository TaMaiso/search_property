from src.data.constants import Env

class MockFindMethodAndHandler:
    def __init__(self, Env, request, path) -> None:
        request_key = Env['METHOD'].value
        path_key = Env['PATH'].value
        request_value = request
        path_value = path
        self.env = {
            request_key: request_value,
            path_key: path_value
        }
        self.response = (request_value, path_value)
    
    def get_env(self):
        return self.env
    
    def get_response(self):
        return self.response