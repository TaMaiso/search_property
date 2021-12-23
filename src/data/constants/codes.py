from enum import Enum

class Codes(Enum):
    OK = '200 OK'
    CREATED = '201 Created'
    NOT_FOUND = '404 Not Found'
    SEVER_ERROR = '500 Internal Server Error'