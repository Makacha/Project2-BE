from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.models import Project
from app.models.base import Base


class Plan(Base):
    __tablename__ = "plan"

    project_id = Column(ForeignKey(Project.id), nullable=False)
    project = relationship(Project)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
