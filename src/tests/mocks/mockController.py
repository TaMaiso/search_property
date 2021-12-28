
class MockController:
    def __init__(self, request) -> None:
        self.year = request.get("year", [""])[0]
        self.city = request.get('city', [""])[0]
        self.price = request.get('price', [""])[0]

    def get_params(self):
        return self.year, self.city, self.price
