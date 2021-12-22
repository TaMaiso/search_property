from enum import Enum 

class Env(Enum):
    PATH = 'PATH_INFO'
    METHOD = 'REQUEST_METHOD'
    STRING = 'QUERY_STRING'
    LENGTH = 'CONTENT_LENGTH'
    INPUT = 'wsgi.input'