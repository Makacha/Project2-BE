from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import get_user_info, get_project_info
from app.database.database import get_db
from app.schemas.pagination_schemas import SearchingPaginationParams
from app.schemas.project_schemas import ProjectCreate, ProjectResponse, ProjectRequest
from app.schemas.response_schemas import DataResponse, PagingDataResponse
from app.schemas.user_schemas import AccessResponse
from app.services.project import ProjectService

router = APIRouter()


@router.get("", response_model=PagingDataResponse[ProjectResponse])
def search_project(*, db: Session = Depends(get_db), user_id=Depends(get_user_info),
                   params=Depends(SearchingPaginationParams)):
    result = ProjectService.search_project(db=db, params=params)
    return PagingDataResponse().success_response(result.items, result.metadata)


@router.get("/{project_id}", response_model=DataResponse[ProjectResponse])
def detail_project(*, db: Session = Depends(get_db), user_id=Depends(get_user_info), project_id: int):
    result = ProjectService.detail_project(db=db, project_id=project_id, user_id=user_id)
    return DataResponse().success_response(result)


@router.post("", response_model=DataResponse[ProjectResponse])
def create_project(*, db: Session = Depends(get_db), user_id=Depends(get_user_info), project_create: ProjectCreate):
    result = ProjectService.create_project(db=db, project_create=project_create, user_id=user_id)
    return DataResponse().success_response(result)


@router.get("/access/{project_id}", response_model=DataResponse[AccessResponse])
def access_project(*, db: Session = Depends(get_db), user_id=Depends(get_user_info), project_id: int):
    result = ProjectService.access_project(db=db, user_id=user_id, project_id=project_id)
    return DataResponse().success_response(result)


@router.post("/request", response_model=DataResponse[AccessResponse])
def request_project(*, db: Session = Depends(get_db), user_id=Depends(get_user_info), project_request: ProjectRequest):
    result = ProjectService.request_project(db=db, user_id=user_id, project_request=project_request)
    return DataResponse().success_response(result)

@router.put("")
def update_project(*, db: Session = Depends(get_db)):
    pass
