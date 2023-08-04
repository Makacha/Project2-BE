from app.crud.crud_base import CRUDBase
from app.models.work_history import WorkHistory


class CRUDWorkHistory(CRUDBase):
    pass


crud_work_history = CRUDWorkHistory(WorkHistory)
