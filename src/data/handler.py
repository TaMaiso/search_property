import re
import json
from typing import List
from urllib.parse import parse_qs
from collections import defaultdict
from collections.abc import Callable
from wsgiref.simple_server import make_server
from .constants import Env, Codes, Methods, Status

class Handler:
    handler_map = defaultdict(dict)
    
    def register(self, method_name: str, path: str, handler: Callable) -> None:
        self.handler_map[fr'^{path}$'].update({method_name: handler})
        return self

    def find_method_path(self, env: dict) -> List[str]:
        request = Env['METHOD'].value
        path = Env['PATH'].value
        return env[request].lower(), env[path]

    def find_status_body_handler(self, path: str, env: dict, method: str) -> List[str]:
        string = Env['STRING'].value
        input = Env['INPUT'].value
        lenght = Env['LENGTH'].value
        request_body_map = {
            Methods['GET'].value: lambda: [Codes['OK'].value, env[string]],
            Methods['POST'].value: lambda: [Codes['CREATED'].value, env[input].read(int(env.get(lenght, 0))).decode()],
        }
        for pattern, info in self.handler_map.items():
            matched = re.match(pattern, path)
            if matched:
                status, request_body  = request_body_map[method]()
                return status, request_body, info[method]
        return Codes['NOT_FOUND'].value, {}, lambda x: ['', 'error', Status['FAIL'].value, None]

    def make_response(self, code: str, msg: str, status: str, data: dict) -> str:
        return json.dumps({
            "code": code,
            "message": msg,
            "data": data,
            "status": status
        })

    def __call__(self, env, start_response):
        method, path = self.find_method_path(env)
        init_code, request_body, handler  = self.find_status_body_handler(path, env, method)
        res_code, msg, status, data = handler(parse_qs(request_body))
        code = res_code if res_code else init_code
        start_response(code, headers=[('Content-Type', 'application/json')])
        response = self.make_response(code, msg, status, data)
        return [response.encode()]

    def get(self, path, handler) -> None:
        return self.register('get', path, handler)

    def post(self, path, handler) -> None:
        return self.register('post', path, handler)

    def start(self) -> None:
        with make_server('localhost', 8088, self) as server:
            server.serve_forever()