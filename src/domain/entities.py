from .valueObjects import Status

class Property:
    def __init__(
        self, 
        id: int, 
        address: str,
        city: str, 
        price: int, 
        description: str, 
        status: str
    ) -> None:
        self.id = id 
        self.address = address
        self.city = city
        self.price = price
        self.description = description 
        self.status = status

class Restrictions:
    def __init__(self)-> None:
        self.viewable = [
            Status['PRESALE'].value, 
            Status['ONSALE'].value, 
            Status['SOLD'].value
        ]

    def get_filter(self):
        return "WHERE sh.status_id = {} OR sh.status_id = {} OR sh.status_id = {}".format(*self.viewable)