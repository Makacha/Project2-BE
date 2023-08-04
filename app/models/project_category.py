from sqlalchemy import Column, ForeignKey

from app.models.base import Base
from app.models.category import Category
from app.models.project import Project


class ProjectCategory(Base):
    __tablename__ = "project_category"

    project_id = Column(ForeignKey(Project.id), nullable=False)
    category_id = Column(ForeignKey(Category.id), nullable=False)
