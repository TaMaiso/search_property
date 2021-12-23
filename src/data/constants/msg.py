from enum import Enum

class Msgs(Enum):
    OK = "Everything's okay"
    CREATED = "Record was created successfully"
    NOT_FOUND = "Path couldn't be found"
    PROBLEM_FOUND = "A problem was found, it was just reported. Please try later"


