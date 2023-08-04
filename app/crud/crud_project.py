from app.crud.crud_base import CRUDBase
from app.models import Project


class CRUDProject(CRUDBase):
    pass


crud_project = CRUDProject(Project)
