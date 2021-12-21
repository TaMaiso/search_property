from ..data import Handler

class App: 
    def __init__(self, config):
        app = Handler(config).get('/things', self.create_things)
        app.start()

    def create_things(self, request):
        return '{"hola": "como estas"}'
        