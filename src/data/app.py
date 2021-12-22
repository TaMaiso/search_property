from .handler import Handler
from .database import  Database
from ..deal import get_params_property

class App: 
    def __init__(self, config):
        app = Handler()
        app.get('/property', self.create_things)
        self.db = Database(config)
        app.start()
    
    def create_things(self, request):
        params = get_params_property(request)
        data = self.db.query(*params)
        return "200 OK", "asdfasdf", "asdfasdfddd", data
        