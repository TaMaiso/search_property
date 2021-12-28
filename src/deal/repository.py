from ..domain import Restrictions

class Repository():
    def __init__(self, year: str="", city: str="", price: str="") -> None:
        self.restrictions = Restrictions().get_filter()
        self.year = year
        self.city = city
        self.price = price

    def filter_by_year(self) -> str:
        return "property.year = {}".format(self.year)

    def filter_by_city(self) -> str:
        return "property.city = '{}'".format(self.city)

    def filter_by_price(self) -> str:
        return "property.price > {}".format(self.price)

    def get_filters(self) -> str:
        is_year_empty = not bool(len(str.strip(self.year)))
        is_city_empty = not bool(len(str.strip(self.city)))
        is_price_empty = not bool(len(str.strip(self.price)))
        if(is_year_empty and is_city_empty and is_price_empty):
            return ""
        if(is_year_empty and is_city_empty):
            return "WHERE {}".format(self.filter_by_price())
        if(is_year_empty and is_price_empty):
            return "WHERE {}".format(self.filter_by_city())
        if(is_city_empty and is_price_empty):
            return "WHERE {}".format(self.filter_by_year())
        if(is_year_empty):
            return "WHERE {} AND {}".format(
                self.filter_by_city(),
                self.filter_by_price()
            )
        if(is_city_empty):
            return "WHERE {} AND {}".format(
                self.filter_by_year(),
                self.filter_by_price()
            )
        if(is_price_empty):
            return "WHERE {} AND {}".format(
                self.filter_by_year(),
                self.filter_by_city()
            )
        return "WHERE {} AND {} AND {}".format(
            self.filter_by_year(),
            self.filter_by_city(),
            self.filter_by_price()
        )
    
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
        """.format(self.restrictions, self.get_filters())