from sqlalchemy.orm import Session

from app.crud import crud_work
from app.schemas.work_schemas import WorkCreate


class WorkService:

    @classmethod
    def create_work(cls, db: Session, work_create: WorkCreate, user_id: int, project_id: int):
        work_create.project_id = project_id
        work_create.owner_id = user_id
        work = crud_work.create(db=db, obj_in=work_create, by_alias=False)
        return work
