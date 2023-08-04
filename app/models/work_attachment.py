from sqlalchemy import Column, ForeignKey, String

from app.models import Work
from app.models.base import Base


class WorkAttachment(Base):
    __tablename__ = "work_attachment"

    work_id = Column(ForeignKey(Work.id), nullable=False)
    link = Column(String(255), nullable=False)
