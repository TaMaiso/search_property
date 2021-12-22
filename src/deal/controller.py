from ..data import Handler, Database

class App: 
    def __init__(self, config):
        app = Handler()
        app.get('/property', self.create_things)
        self.db = Database(config)
        app.start()

    def create_things(self, request):
        year = request['year'][0]
        city = request['city'][0]
        price = request['price'][0]
        data = self.db.query(year, "'{}'".format(city), price)
        print(data)
        return "200 OK", "asdfasdf", "asdfasdfddd", data
        