import hashlib

from sqlalchemy.orm import Session

from app.core.security import create_access_token
from app.crud import crud_user, crud_member
from app.helpers.exception_type import ExceptionType
from app.schemas.exception_schemas import AppException
from app.schemas.user_schemas import UserCreate, LoginRequest, AccessResponse, SearchUserParams


class UserService:

    @classmethod
    def login(cls, db: Session, login_request: LoginRequest):
        user = crud_user.get_by_username(db=db, username=login_request.username)
        if not user:
            raise AppException(ExceptionType.LOGIN_FAILED)
        login_request.password = hashlib.sha256(login_request.password.encode()).hexdigest()
        if user.password != login_request.password:
            raise AppException(ExceptionType.LOGIN_FAILED)
        return AccessResponse(**{
            'token': create_access_token(user.id)
        })

    @classmethod
    def create_user(cls, db: Session, user_form: UserCreate):
        user = crud_user.get_by_username(db=db, username=user_form.username)
        if user:
            raise AppException(ExceptionType.USERNAME_EXISTED)
        user = crud_user.get_by_email(db=db, email=user_form.email)
        if user:
            raise AppException(ExceptionType.EMAIL_EXISTED)
        user_form.password = hashlib.sha256(user_form.password.encode()).hexdigest()
        user = crud_user.create(db=db, obj_in=user_form, by_alias=False)
        return user

    @classmethod
    def get_current_user_info(cls, db: Session, user_id: int):
        user = crud_user.get(db=db, identification=user_id)
        if not user:
            raise AppException(ExceptionType.TOKEN_INVALID)
        return user

    @classmethod
    def search_user(cls, db: Session, params: SearchUserParams, project_id: int = None):
        users = crud_user.search(db=db, params=params, project_id=project_id)
        if project_id:
            for user in users.items:
                member = crud_member.get_by_user_id_and_project_id(db=db, user_id=user.id, project_id=project_id)
                user.project_id = member.project_id
                user.role = member.role.value
        return users
