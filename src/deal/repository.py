from ..domain import PropRestrictions, PropFilters

class Repository():
    def __init__(self, year: str="", city: str="", price: str="") -> None:
        self.restrictions = PropRestrictions().get_filter()
        self.filters = PropFilters(year, city, price).get_filters()

    def get_query(self):
        return """\
            SELECT property.id, property.address, property.city, property.price, property.description, status.name AS status\
            FROM habi_db.status_history AS history\
            INNER JOIN (\
                SELECT sh.property_id AS id, MAX(sh.update_date) AS date\
                FROM habi_db.status_history AS sh\
                {}\
                GROUP BY sh.property_id)\
            AS sh ON (\
                sh.id = history.property_id and sh.date = history.update_date)\
            INNER JOIN habi_db.property AS property\
            ON property.id = history.property_id\
            INNER JOIN habi_db.status AS status\
            ON status.id  = history.status_id\
            {}\
        """.format(self.restrictions, self.filters)