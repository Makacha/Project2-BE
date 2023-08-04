from sqlalchemy.orm import Session

from app.crud import crud_plan
from app.schemas.plan_schemas import PlanCreate


class PlanService:

    @classmethod
    def create_plan(cls, db: Session, plan_create: PlanCreate, user_id: int, project_id: int):
        plan_create.project_id = project_id
        plan = crud_plan.create(db=db, obj_in=plan_create, by_alias=False)
        return plan
