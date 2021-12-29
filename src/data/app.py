from .handler import Handler
from .database import  Database
from ..deal import Controller
from ..deal import Repository

class App: 
    def __init__(self, config):
        app = Handler()
        app.get('/property', self.get_properties)
        self.db = Database(config)
        app.start()
    
    def get_properties(self, request):
        params = Controller(request).get_params()
        statement = Repository(*params).get_query()
        code, message, status, data = self.db.query(statement)
        return code, message, status, data
        