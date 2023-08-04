import enum

from sqlalchemy import Column, String, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship

from app.models import User, Project
from app.models.base import Base


class DocumentStatus(enum.Enum):
    DRAFT = "Nháp"
    READY = "Hoàn thiện"
    OFFICIAL = "Chính thức"
    DEPRECATED = "Ngừng sử dụng"


class Document(Base):
    __tablename__ = "document"

    project_id = Column(ForeignKey(Project.id))
    project = relationship(Project)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    content = Column(Text, nullable=False)
    status = Column(Enum(DocumentStatus, values_callable=lambda x: [e.value for e in DocumentStatus]), nullable=False,
                    default=DocumentStatus.DRAFT)

    owner_id = Column(ForeignKey(User.id), nullable=False)
    owner = relationship(User)

