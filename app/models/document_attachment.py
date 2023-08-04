from sqlalchemy import Column, ForeignKey, String

from app.models.base import Base
from app.models.document import Document


class DocumentAttachment(Base):
    __tablename__ = "document_attachment"

    document_id = Column(ForeignKey(Document.id), nullable=False)
    link = Column(String(255), nullable=False)
