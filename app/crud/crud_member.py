from sqlalchemy.orm import Session

from app.crud.crud_base import CRUDBase
from app.models import Member


class CRUDMember(CRUDBase):

    def get_by_user_id_and_project_id(self, db: Session, user_id: int, project_id: int):
        return db.query(self.model).filter(Member.user_id == user_id).filter(Member.project_id == project_id).first()


crud_member = CRUDMember(Member)
