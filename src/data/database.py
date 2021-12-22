from MySQLdb import _mysql

class Database:
    def __init__(self, config):
        self.host = config['HOST']
        self.port = config['PORT']
        self.user = config['USER']
        self.password = config['PASSWORD']
        self.database = config['DATABASE']
        self.db = self.start()

    def start(self):
        return _mysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )
    
    def query(self, query):
        self.db.query()