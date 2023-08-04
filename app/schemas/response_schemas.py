from typing import TypeVar, Generic, Sequence, Optional, Union

from pydantic import BaseModel
from pydantic.generics import GenericModel

from app.schemas.pagination_schemas import Pagination

T = TypeVar("T")


class ResponseSchemaBase(BaseModel):
    __abstract__ = True

    code: str = ""
    message: str = ""


class ResponseBase(ResponseSchemaBase):

    def custom_response(self, code: str, message: str):
        self.code = code
        self.message = message
        return self

    def success_response(self):
        self.code = '000'
        self.message = 'Thành công'
        return self

    def fail_response(self, code: str, message: str):
        self.code = code
        self.message = message
        return self


class DataResponse(ResponseSchemaBase, GenericModel, Generic[T]):
    data: Optional[T] = None

    class Config:
        arbitrary_types_allowed = True

    def custom_response(self, code: str, message: str, data: T):
        self.code = code
        self.message = message
        self.data = data
        return self

    def success_response(self, data: Optional[T]):
        self.code = '000'
        self.message = 'Thành công'
        self.data = data
        return self

    def fail_response(self, code: str, message: str, data: T = None):
        self.code = code
        self.message = message
        self.data = data
        return self


class DataResponseList(ResponseSchemaBase, GenericModel, Generic[T]):
    data: dict = None

    class Config:
        arbitrary_types_allowed = True

    def success_response(self, data: Sequence[T]):
        self.code = '000'
        self.message = 'Thành công'
        self.data = {
            'total': len(data),
            'items': data
        }
        return self

    def fail_response(self, code: str, message: str, data: Sequence[T]):
        self.code = code
        self.message = message
        self.data = {
            'total': len(data),
            'items': data
        }
        return self


class PagingDataResponse(ResponseSchemaBase, GenericModel, Generic[T]):
    data: Optional[Sequence[T]] = None
    metadata: Optional[Pagination] = None

    def success_response(self, data: Sequence[T], metadata: Pagination):
        self.code = "000"
        self.message = "Thành công"
        self.data = data
        self.metadata = metadata
        return self
