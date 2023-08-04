from sqlalchemy import Column, String

from app.models.base import Base


class Category(Base):
    __tablename__ = "category"

    code = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
