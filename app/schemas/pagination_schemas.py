from contextvars import ContextVar
from typing import Optional, Type, Sequence, TypeVar, Generic

from pydantic import BaseModel, root_validator
from pydantic.generics import GenericModel

from app.helpers.exception_type import ExceptionType
from app.schemas.exception_schemas import AppException

T = TypeVar("T")
C = TypeVar("C")


class Pagination(BaseModel):
    current_page: int
    page_size: int
    total_items: int

    class Config:
        fields = {
            'current_page': 'currentPage',
            'page_size': 'pageSize',
            'total_items': 'totalItems',
        }
        allow_population_by_field_name = True


class Page(GenericModel, Generic[T]):
    items: Sequence[T]
    metadata: Pagination

    @classmethod
    def create(cls, items: Sequence[T], metadata: Pagination) -> "Page[T]":
        return cls(
            items=items,
            metadata=metadata
        )


PageType: ContextVar[Type[Page]] = ContextVar("PageType", default=Page)


class PaginationParams(BaseModel):
    page_size: Optional[int] = 10
    page: Optional[int] = 1
    sort_by: Optional[str] = 'id'
    direction: Optional[str] = 'desc'

    class Config:
        fields = {
            'page_size': 'pageSize',
            'sort_by': 'sortBy'
        }
        allow_population_by_field_name = True


class SearchingPaginationParams(PaginationParams):
    field_values: str = ""
    operators: str = ""
    values: str = ""

    class Config:
        fields = {
            'field_values': 'fields'
        }
        allow_population_by_field_name = True

    @root_validator
    def validate_data(cls, data):
        field_values = data.get("field_values").split("|") if data.get("field_values") else []
        operators = data.get("operators").split("|") if data.get("operators") else []
        values = data.get("values").split("|") if data.get("values") else []
        if len(field_values) != len(operators) != len(values):
            raise AppException(ExceptionType.INVALID_SEARCH_PARAM)
        return data

