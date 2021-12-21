import re
from urllib.parse import parse_qs
from collections import defaultdict
from wsgiref.simple_server import make_server

class Base:
    handler_map = defaultdict(dict)
    status_map = { 'get': '200 OK', 'post': '201 Created' }
    
    def _register(self, method_name, path, handler):
        self.handler_map[fr'^{path}$'].update({method_name: handler})
        return self

    def get(self, path, handler):
        return self._register('get', path, handler)


    def post(self, path, handler):
        return self._register('post', path, handler)

    def _handler_defaulft(self, request, **args):
        print(request, args)
        return '{"data": "not found"}'

    def _find_handler(self, path, method):
        for pattern, info in self.handler_map.items():
            matched = re.match(pattern, path)
            if matched:
                return info[method], matched.groupdict()
        return self._handler_defaulft, {}

    def _find_status(self, method):
        methods = self.status_map.keys()
        if(method in methods):
            return self.status_map[method]
        return '404 not found'

    def _find_request_body(self, method, environment):
        request_body_map = {
            'get': lambda: environment['QUERY_STRING'],
            'post': lambda: environment['wsgi.input'].read(int(environment.get('CONTENT_LENGTH', 0))).decode(),
        }
        requests =  request_body_map.keys()
        if(method in requests):
            return request_body_map[method]()
        return lambda: {}

    def __call__(self, environment, start_response):
        method = environment['REQUEST_METHOD'].lower()
        path = environment['PATH_INFO']
        status = self._find_status(method)
        request_body = self._find_request_body(method, environment)
        handler, path_params = self._find_handler(path, method)
        response = handler(parse_qs(request_body), **path_params)
        start_response(status, headers=[('Content-Type', 'application/json')])
        return [response.encode()]


    def start(self):
        with make_server('localhost', 8088, self) as server:
            print(self.handler_map)
            server.serve_forever()