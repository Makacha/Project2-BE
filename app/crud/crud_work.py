import json

from sqlalchemy.orm import Session

from app.crud.crud_base import CRUDBase
from app.crud.crud_work_history import crud_work_history
from app.models import Work


class CRUDWork(CRUDBase):

    def create(self, db: Session, obj_in, **data):
        work = super().create(db=db, obj_in=obj_in, data=data)
        crud_work_history.create(db=db,
                                 obj_in={
                                     "origin": None,
                                     "change": json.dumps(obj_in),
                                     "work_id": work.id
                                 })
        return work

    def update(self, db: Session, db_obj, obj_in):
        obj_data = db_obj.as_dict()
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        origin = {}
        change = {}
        for field in obj_data:
            if field in update_data and obj_data[field] != update_data[field]:
                origin[field] = obj_data[field]
                change[field] = update_data[field]
        work = super().update(db=db, db_obj=db_obj, obj_in=obj_in)
        crud_work_history.create(db=db,
                                 obj_in={
                                     "origin": json.dumps(origin),
                                     "change": json.dumps(change),
                                     "work_id": work.id
                                 })
        return work


crud_work = CRUDWork(Work)
