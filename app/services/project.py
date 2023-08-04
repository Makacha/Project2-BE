from datetime import datetime

from sqlalchemy.orm import Session

from app.core.security import create_access_token
from app.crud import crud_project, crud_member
from app.helpers.exception_type import ExceptionType
from app.models.member import MemberRole, MemberStatus
from app.schemas.exception_schemas import AppException
from app.schemas.pagination_schemas import SearchingPaginationParams
from app.schemas.project_schemas import ProjectCreate, ProjectRequest
from app.schemas.user_schemas import AccessResponse


class ProjectService:

    @classmethod
    def create_project(cls, db: Session, project_create: ProjectCreate, user_id: int):
        categories = project_create.categories
        del project_create.categories
        project = crud_project.create(db=db, obj_in=project_create, by_alias=False)
        crud_member.create(db=db, obj_in={
            "project_id": project.id,
            "user_id": user_id,
            "role": MemberRole.OWNER,
            "join_date": datetime.now(),
            "status": MemberStatus.ACTIVE,
        })
        return project

    @classmethod
    def search_project(cls, db: Session, params: SearchingPaginationParams):
        return crud_project.search(db=db, params=params)

    @classmethod
    def detail_project(cls, db: Session, project_id: int, user_id: int):
        project = crud_project.get(db=db, identification=project_id)
        if not project:
            raise AppException(ExceptionType.PROJECT_NOT_FOUND)
        member = crud_member.get_by_user_id_and_project_id(db=db, user_id=user_id, project_id=project_id)
        if member:
            project.role = member.role.value
            project.member_status = member.status.value
        return project

    @classmethod
    def update_project(cls, db: Session, project_id, project_update):
        categories = project_update.categories
        project = crud_project.get(db=db, id=project_id)
        if not project:
            raise AppException(ExceptionType.PROJECT_NOT_FOUND)
        project = crud_project.update(db=db, obj_in=project_update, by_alias=False)
        return project

    @classmethod
    def access_project(cls, db: Session, user_id: int, project_id: int):
        member = crud_member.get_by_user_id_and_project_id(db=db, user_id=user_id, project_id=project_id)

        if not member:
            raise AppException(ExceptionType.PROJECT_ACCESS_DENIED)

        return AccessResponse(**{
            'token': create_access_token(user_id, project_id),
            'role': member.role.value
        })

    @classmethod
    def request_project(cls, db: Session, user_id: int, project_request: ProjectRequest):
        project = crud_project.get(db=db, identification=project_request.project_id)
        if not project:
            raise AppException(ExceptionType.PROJECT_NOT_FOUND)
        member = crud_member.get_by_user_id_and_project_id(
            db=db, user_id=user_id, project_id=project.id)

        if not member:
            crud_member.create(db=db, obj_in={
                "project_id": project.id,
                "user_id": user_id,
                "role": MemberRole.MEMBER if not project_request.role else project_request.role,
                "join_date": datetime.now(),
                "status": MemberStatus.WAITING,
            })
        else:
            crud_member.update(db=db, db_obj=member, obj_in={
                "role": MemberRole.MEMBER if not project_request.role else project_request.role,
                "status": MemberStatus.WAITING
            })
