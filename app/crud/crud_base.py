from typing import Generic, TypeVar, Type, Any, Optional, Union, Dict

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session, Query

from app.helpers import constants
from app.models.base import Base
from app.schemas.pagination_schemas import PaginationParams, Page, Pagination, PageType, SearchingPaginationParams

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, identification: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == identification).first()

    def create(self, db: Session, *, obj_in: CreateSchemaType, **data) -> ModelType:
        if data.get('by_alias') is not None:
            obj_in_data = jsonable_encoder(obj_in, by_alias=data.get('by_alias'))
        else:
            obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
            self,
            db: Session,
            *,
            db_obj: ModelType,
            obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = db_obj.as_dict()
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, *, identification: int) -> ModelType:
        obj = db.query(self.model).get(identification)
        db.delete(obj)
        db.commit()
        return obj

    def paginate(self, query: Query, params: PaginationParams) -> Page:
        total = query.count()

        order_field_model = getattr(self.model, params.sort_by)
        if params.direction == 'desc':
            query = query.order_by(order_field_model.desc())
        else:
            query = query.order_by(order_field_model.asc())
        items = query.offset(params.page_size * (params.page - 1)).limit(params.page_size).all()
        pagination = Pagination(
                current_page=params.page,
                page_size=params.page_size,
                total_items=total
            )
        return PageType.get().create(items=items, metadata=pagination)

    def filter_equal(self, query, field, value):
        f = getattr(self.model, field)
        return query.filter(f == value)

    def filter_not_equal(self, query, field, value):
        f = getattr(self.model, field)
        return query.filter(f != value)

    def filter_like(self, query, field, value):
        f = getattr(self.model, field)
        return query.filter(f.ilike('%' + value + '%'))

    def filter_greater(self, query, field, value):
        f = getattr(self.model, field)
        return query.filter(f > value)

    def filter_greater_or_equal(self, query, field, value):
        f = getattr(self.model, field)
        return query.filter(f >= value)

    def filter_less_than(self, query, field, value):
        f = getattr(self.model, field)
        return query.filter(f < value)

    def filter_less_than_or_equal(self, query, field, value):
        f = getattr(self.model, field)
        return query.filter(f <= value)

    def filter_in_list(self, query, field, value):
        f = getattr(self.model, field)
        if type(value) != list:
            value = value.split(",")
        return query.filter(f.in_(value))

    def add_filter(self, query, field, value, compare_type):
        if value is None:
            return query
        switch = {
            constants.Compare.EQUAL: self.filter_equal,
            constants.Compare.NOT_EQUAL: self.filter_not_equal,
            constants.Compare.LIKE: self.filter_like,
            constants.Compare.GREATER: self.filter_greater,
            constants.Compare.GREATER_EQUAL: self.filter_greater_or_equal,
            constants.Compare.LESS: self.filter_less_than,
            constants.Compare.LESS_EQUAL: self.filter_less_than_or_equal,
            constants.Compare.IN_LIST: self.filter_in_list,
        }
        filter_func = switch.get(compare_type)
        if filter_func is not None:
            return filter_func(query=query, field=field, value=value)
        return None

    def get_by_fields(self, db: Session, fields: str = None, operators: str = None, values: str = None,
                      order_field: str = None, direction: str = None, limit: str = None):
        # Filter query
        query = db.query(self.model)
        if fields:
            fields = fields.split('|')
            operators = operators.split('|')
            values = values.split('|')
            for field, operator, value in list(zip(fields, operators, values)):
                query = self.add_filter(query, field, value, operator)

        # Order query
        if order_field:
            order_field_model = getattr(self.model, order_field)
            if direction == 'desc':
                query = query.order_by(order_field_model.desc())
            else:
                query = query.order_by(order_field_model.asc())
        if limit:
            query = query.limit(limit)
        return query

    def search(self, db: Session, params: SearchingPaginationParams):
        query = self.get_by_fields(db=db, fields=params.field_values, operators=params.operators, values=params.values)
        return self.paginate(query=query, params=params)
