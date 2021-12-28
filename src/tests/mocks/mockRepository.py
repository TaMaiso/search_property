class MockRepository:
    def __init__(self, year: str="", city: str="", price: str="") -> None:
        self.year = year
        self.city = city
        self.price = price
    
    def get_params(self):
        return self.year, self.city, self.price
    
    def get_filters(self):
        is_year_empty = not bool(len(str.strip(self.year)))
        is_city_empty = not bool(len(str.strip(self.city)))
        is_price_empty = not bool(len(str.strip(self.price)))
        if(is_year_empty and is_city_empty and is_price_empty):
            return ""
        if(is_year_empty and is_city_empty):
            return "WHERE property.price > {}".format(self.price)
        if(is_year_empty and is_price_empty):
            return "WHERE property.city = '{}'".format(self.city)
        if(is_city_empty and is_price_empty):
            return "WHERE property.year = {}".format(self.year)
        if(is_year_empty):
            return "WHERE property.city = '{}' AND property.price > {}".format(
                self.city,
                self.price
            )
        if(is_city_empty):
            return "WHERE property.year = {} AND property.price > {}".format(
                self.year,
                self.price
            )
        if(is_price_empty):
            return "WHERE property.year = {} AND property.city = '{}'".format(
                self.year,
                self.city
            )
        return "WHERE property.year = {} AND property.city = '{}' AND property.price > {}".format(
            self.year,
            self.city,
            self.price
        )