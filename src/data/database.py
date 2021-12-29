import pymysql
import logging 
from ..domain import Property
from .valueObjects import Status, Msgs, Codes

class Database:
    def __init__(self, config):
        self.host = config['HOST']
        self.port = int(config['PORT'])
        self.user = config['USER']
        self.password = config['PASSWORD']
        self.database = config['DATABASE']

    def query(self, statement):
        try: 
            connect = pymysql.Connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            logging.info('ok:', 'connection reset', {})
            with connect.cursor() as cursor:
                cursor.execute(statement)
                properties = []
                for aaa in cursor.fetchall():
                    prop = Property(*aaa)
                    properties.append(prop.__dict__)

            return Codes['OK'].value, Msgs['OK'].value, Status['SUCCESS'].value, properties

        except pymysql.err.OperationalError as err:           
            logging.error('Protocol problem:', 'connection reset', extra=err)
            return Codes['SEVER_ERROR'].value, Msgs['PROBLEM_FOUND'].value, Status['ERROR'].value, None


        finally:
            cursor.close()
            connect.close()