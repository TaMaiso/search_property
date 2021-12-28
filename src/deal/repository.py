
class Repository():
    def __init__(self, year: str="", city: str="", price: str="") -> None:
        self.year = year
        self.city = city
        self.price = price

    def filter_by_year(self) -> str:
        return "property.year = {}".format(self.year)

    def filter_by_city(self) -> str:
        return "property.city = '{}'".format(self.city)

    def filter_by_price(self) -> str:
        return "property.price = {}".format(self.price)

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