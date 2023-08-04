import re


def _regex(pattern: str, value: str):
    if re.compile(pattern).fullmatch(value):
        return True
    return False


def validate_email(email: str):
    return _regex(pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", value=email)


def validate_phone(phone: str):
    return _regex(pattern=r"^0[0-9]{9,11}$", value=phone)


def validate_name(name: str):
    pattern = r"^[a-zA-Z_ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀẾỂưạảấầẩẫậắằẳẵặẹẻẽềếể" \
              r"ỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵýỷỹ\s]+$"
    return _regex(pattern=pattern, value=name)


def validate_username(username: str):
    return _regex(pattern=r"^[a-z0-9]+$", value=username)


def validate_password(password: str):
    return _regex(pattern=r"^\S$", value=password)
