from typing import Optional

from pydantic import BaseModel, root_validator

from app.helpers.exception_type import ExceptionType
from app.helpers.utils import validate_email, validate_phone, validate_username
from app.models.member import MemberStatus
from app.schemas.exception_schemas import AppException
from app.schemas.pagination_schemas import SearchingPaginationParams


class UserCreate(BaseModel):
    username: str
    fullname: str
    password: str
    email: str
    phone: Optional[str]

    class Config:
        fields = {
            'fullname': 'fullName'
        }
        allow_population_by_field_name = True

    @root_validator()
    def validate_date(cls, values):
        values['fullname'] = values['fullname'].strip()
        if not validate_email(values['email']):
            raise AppException(ExceptionType.INVALID_EMAIL)
        if values['phone'] and not validate_phone(values['phone']):
            raise AppException(ExceptionType.INVALID_PHONE)
        if not validate_username(values['username']):
            raise AppException(ExceptionType.INVALID_USERNAME)
        return values


class UserResponse(BaseModel):
    id: int
    username: str
    fullname: str
    email: str
    phone: Optional[str]
    project_id: Optional[int]
    role: Optional[str]

    class Config:
        fields = {
            "project_id": "projectId",
            "fullname": "fullName",
        }
        orm_mode = True
        allow_population_by_field_name = True


class LoginRequest(BaseModel):
    username: str
    password: str

    @root_validator()
    def validate_date(cls, values):
        return values


class AccessResponse(BaseModel):
    token: str
    role: Optional[str]


class SearchUserParams(SearchingPaginationParams):
    role: Optional[str]
    status: Optional[str] = MemberStatus.ACTIVE.value

    class Config:
        allow_population_by_field_name = True

    @root_validator()
    def validate_data(cls, data):
        super().validate_data(data)
        fields = data.get("field_values").split("|") if data.get("field_values") else []
        operators = data.get("operators").split("|") if data.get("operators") else []
        values = data.get("values").split("|") if data.get("values") else []
        tmp_f = tmp_o = tmp_v = ""
        for i in range(len(fields)):
            if fields[i] == "role":
                data['role'] = values[i].split(',')
            elif fields[i] == "status":
                data['status'] = values[i]
            else:
                tmp_f += fields[i] + "|"
                tmp_o += operators[i] + "|"
                tmp_v += values[i] + "|"
        data['field_values'] = tmp_f[:-1]
        data['operators'] = tmp_o[:-1]
        data['values'] = tmp_v[:-1]
        return data
