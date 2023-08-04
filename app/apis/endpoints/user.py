from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import get_user_info, get_project_info
from app.database.database import get_db
from app.helpers.exception_type import ExceptionType
from app.schemas.exception_schemas import AppException
from app.schemas.response_schemas import DataResponse, PagingDataResponse
from app.schemas.user_schemas import UserCreate, LoginRequest, UserResponse, AccessResponse, SearchUserParams
from app.services.user import UserService

router = APIRouter()


@router.post("/signup", response_model=DataResponse[UserResponse])
def create_user(*, db: Session = Depends(get_db), user_form: UserCreate):
    result = UserService.create_user(db=db, user_form=user_form)

    return DataResponse().success_response(result)


@router.post("/login", response_model=DataResponse[AccessResponse])
def login(*, db: Session = Depends(get_db), login_request: LoginRequest):
    result = UserService.login(db=db, login_request=login_request)

    return DataResponse().success_response(result)


@router.get("/info", response_model=DataResponse[UserResponse])
def get_user_info(*, db: Session = Depends(get_db), user_id=Depends(get_user_info)):
    result = UserService.get_current_user_info(db=db, user_id=user_id)
    return DataResponse().success_response(result)


@router.get("", response_model=PagingDataResponse[UserResponse])
def search_user(*, db: Session = Depends(get_db), params: SearchUserParams = Depends(SearchUserParams),
                project_id=Depends(get_project_info)):
    if not project_id:
        raise AppException(ExceptionType.PROJECT_NOT_FOUND)
    result = UserService.search_user(db=db, params=params, project_id=project_id)
    return PagingDataResponse().success_response(result.items, result.metadata)

