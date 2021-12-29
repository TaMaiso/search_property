from ..valueObjects import Status


class PropRestrictions:
    def __init__(self)-> None:
        self.viewable = [
            Status['PRESALE'].value, 
            Status['ONSALE'].value, 
            Status['SOLD'].value
        ]

    def get_filter(self):
        return "WHERE sh.status_id = {} OR sh.status_id = {} OR sh.status_id = {}".format(*self.viewable)
