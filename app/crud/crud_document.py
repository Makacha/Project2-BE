from app.crud.crud_base import CRUDBase
from app.models import Document


class CRUDDocument(CRUDBase):
    pass


crud_document = CRUDDocument(Document)
