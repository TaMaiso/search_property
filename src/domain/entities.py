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
