from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import get_user_info, get_project_info
from app.database.database import get_db
from app.schemas.document_schemas import DocumentCreate, DocumentResponse
from app.schemas.response_schemas import DataResponse
from app.services.document import DocumentService

router = APIRouter()


@router.post("", response_model=DataResponse[DocumentResponse])
def create_document(*, db: Session = Depends(get_db), document_create: DocumentCreate, user_id=Depends(get_user_info),
                    project_id=Depends(get_project_info)):
    result = DocumentService.create_document(db=db, document_create=document_create, user_id=user_id,
                                             project_id=project_id)
    return DataResponse().success_response(result)
