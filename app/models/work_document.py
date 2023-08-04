from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.document import Document
from app.models.work import Work


class WorkDocument(Base):
    __tablename__ = "work_document"

    word_id = Column(ForeignKey(Work.id))
    work = relationship(Work)
    document_id = Column(ForeignKey(Document.id))
    document = relationship(Document)
