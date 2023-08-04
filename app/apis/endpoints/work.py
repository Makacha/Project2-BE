from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import get_user_info, get_project_info
from app.database.database import get_db
from app.schemas.response_schemas import DataResponse
from app.schemas.work_schemas import WorkCreate, WorkResponse
from app.services.work import WorkService

router = APIRouter()


@router.post("", response_model=DataResponse[WorkResponse])
def create_work(*, db: Session = Depends(get_db), work_create: WorkCreate, user_id=Depends(get_user_info),
                project_id=Depends(get_project_info)):
    result = WorkService.create_work(db=db, work_create=work_create, user_id=user_id, project_id=project_id)
    return DataResponse().success_response(result)
