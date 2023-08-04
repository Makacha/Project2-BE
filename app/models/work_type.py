from sqlalchemy import Column, String, ForeignKey

from app.models import Project
from app.models.base import Base


class WorkType(Base):
    __tablename__ = "work_type"

    name = Column(String(255), nullable=False)
    project_id = Column(ForeignKey(Project.id), nullable=False)
