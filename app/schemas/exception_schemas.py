

class AppException(Exception):
    http_code: int
    code: str
    message: str

    def __init__(self, exception_type=None, http_code: int = None, code: str = None, message: str = None):
        if exception_type:
            self.http_code = exception_type.http_code
            self.code = exception_type.code
            self.message = exception_type.message
        else:
            self.http_code = http_code if http_code else 500
            self.code = code if code else str(self.http_code)
            self.message = message

    def __str__(self):
        return self.message
