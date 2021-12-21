from .base import Base

class App: 
    def __init__(self):
        app = Base().get('/things', self.create_things)
        app.start()

    def create_things(self, request):
        return '{"hola": "como estas"}'
        