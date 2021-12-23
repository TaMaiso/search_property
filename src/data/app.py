from .handler import Handler
from .database import  Database
from ..deal import get_params_property

class App: 
    def __init__(self, config):
        app = Handler()
        app.get('/property', self.get_properties)
        self.db = Database(config)
        app.start()
    
    def get_properties(self, request):
        params = get_params_property(request)
        code, message, status, data = self.db.query(*params)
        return code, message, status, data
        