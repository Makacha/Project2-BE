from enum import Enum


class ExceptionType(Enum):

    USERNAME_EXISTED = 400, '001', 'Tên tài khoản đã tồn tại'
    LOGIN_FAILED = 400, '002', 'Tài khoản hoặc mật khẩu không đúng'
    TOKEN_INVALID = 403, '003', 'Access Token không hợp lệ'
    TOKEN_EXPIRED = 403, '004', 'Access Token đã hết hạn'
    EMAIL_EXISTED = 400, '005', 'Email đã được đăng ký'

    PROJECT_NOT_FOUND = 400, '100', 'Project không tồn tại'
    PROJECT_ACCESS_DENIED = 400, '101', 'Không được phép truy cập vào dự án'

    INVALID_EMAIL = 400, '200', 'Email không hợp lệ'
    INVALID_PHONE = 400, '201', 'Số điện thoại không hợp lệ'
    INVALID_NAME = 400, '202', 'Tên không hợp lệ'
    INVALID_USERNAME = 400, '203', 'Tên đăng nhập không hợp lệ'
    INVALID_SEARCH_PARAM = 400, '204', 'Đầu vào tìm kiếm không hợp lệ'

    INTERNAL_SERVER_ERROR = 500, '999', 'Hệ thống đang bảo trì, vui lòng thử lại sau'

    def __new__(cls, *args, **kwargs):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, http_code, code, message):
        self.http_code = http_code
        self.code = code
        self.message = message
