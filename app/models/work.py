from sqlalchemy import Column, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.models import User, Project
from app.models.base import Base


class Work(Base):
    __tablename__ = "work"

    project_id = Column(ForeignKey(Project.id))
    project = relationship(Project)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    content = Column(Text, nullable=False)
    due_date = Column(DateTime, nullable=True)
    owner_id = Column(ForeignKey(User.id), nullable=False)
    owner = relationship(User)
    assignee_id = Column(ForeignKey(User.id), nullable=True)
    assignee = relationship(User)
