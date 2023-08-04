from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import get_project_info, get_user_info
from app.database.database import get_db
from app.schemas.plan_schemas import PlanCreate, PlanResponse
from app.schemas.response_schemas import DataResponse
from app.services.plan import PlanService

router = APIRouter()


@router.post("", response_model=DataResponse[PlanResponse])
def create_plan(*, db: Session = Depends(get_db), plan_create: PlanCreate, user_id=Depends(get_user_info),
                project_id=Depends(get_project_info)):
    result = PlanService.create_plan(db=db, plan_create=plan_create, user_id=user_id, project_id=project_id)
    return DataResponse().success_response(result)
