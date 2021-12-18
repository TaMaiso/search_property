from wsgiref.simple_server import make_server

def application(env, start_response):
    headers = [('Content-Type', 'text/plain')]
    start_response('200 OK', headers)
    return ['Hola'.encode('utf-8')]

with make_server('localhost', 8000, application) as server:
    print("Serving on port 8000")
    server.serve_forever()
