from app.crud.crud_base import CRUDBase
from app.models import Plan


class CRUDPlan(CRUDBase):
    pass


crud_plan = CRUDPlan(Plan)
