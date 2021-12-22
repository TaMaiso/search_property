
class MockGetParamsProperty:
    def __init__(self, year, city, price) -> None:
        self.year = year
        self.city = city
        self.price = price
        self.request = {'year': [year], 'city': [city], 'price': [price]}

    def get_resolve(self):
        return self.year, "'{}'".format(self.city), self.price

    def get_request(self):
        return self.request