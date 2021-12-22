import json

class MockMakeResponse: 
    def __init__(self, code, msg,  status, data) -> None:      
        self.code =  code
        self.msg = msg
        self.data = data
        self.status = status
        self.mock_response = json.dumps({
            "code": self.code ,
            "message": self.msg,
            "data": self.data,
            "status": self.status
        })
    
    def get_params(self):
        return self.code, self.msg, self.status, self.data

    def get_response(self):
        return self.mock_response
