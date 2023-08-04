from sqlalchemy.orm import Session

from app.crud.crud_base import CRUDBase
from app.models import User, Member
from app.schemas.user_schemas import SearchUserParams


class CRUDUser(CRUDBase):

    def get_by_username(self, db: Session, username: str):
        query = db.query(self.model).filter(User.username == username)
        return query.first()

    def get_by_email(self, db: Session, email: str):
        query = db.query(self.model).filter(User.email == email)
        return query.first()

    def search(self, db: Session, params: SearchUserParams, project_id: int = None):
        query = self.get_by_fields(db=db, fields=params.field_values, operators=params.operators, values=params.values)
        if project_id:
            query = query.join(Member).filter(Member.project_id == project_id)
            query = query.filter(Member.status == params.status)
            if params.role:
                query = query.filter(Member.role.in_(params.role))
        return self.paginate(query=query, params=params)


crud_user = CRUDUser(User)
