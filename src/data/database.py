import pymysql
import logging 
from ..domain import Property
from .constants import Status, Msgs, Codes

class Database:
    def __init__(self, config):
        self.host = config['HOST']
        self.port = int(config['PORT'])
        self.user = config['USER']
        self.password = config['PASSWORD']
        self.database = config['DATABASE']

    def query(self,year, city, price):
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
                statement = """
                    SELECT property.id, property.address, property.city, property.price, property.description, status.name AS status
                    FROM habi_db.status_history AS history 
                    INNER JOIN (
                        SELECT sh.property_id AS id, MAX(sh.update_date) AS date 
                        FROM habi_db.status_history AS sh 
                        WHERE (sh.status_id = 3 OR sh.status_id = 4 OR sh.status_id = 5) 
                        GROUP BY sh.property_id) 
                    AS sh ON (
                        sh.id = history.property_id and sh.date = history.update_date)
                    INNER JOIN habi_db.property AS property
                    ON property.id = history.property_id 
                    INNER JOIN habi_db.status AS status
                    ON status.id  = history.status_id 
                    WHERE property.year = {} AND property.city = {}  AND property.price > {}
                """.format(year, city, price)
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