from ..data import Handler

class App: 
    def __init__(self, ):
        app = Handler()
        app.get('/things', self.create_things)
        app.start()

    def create_things(self, request):
        return "200 OK", "asdfasdf", "asdfasdfddd", {"hola": "como estas"}
        