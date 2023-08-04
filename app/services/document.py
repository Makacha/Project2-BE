from sqlalchemy.orm import Session

from app.crud import crud_document
from app.schemas.document_schemas import DocumentCreate


class DocumentService:

    @classmethod
    def create_document(cls, db: Session, document_create: DocumentCreate, user_id: int, project_id: int):
        document_create.project_id = project_id
        document_create.owner_id = user_id
        document = crud_document.create(db=db, obj_in=document_create, by_alias=False)
        return document
