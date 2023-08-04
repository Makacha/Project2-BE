from sqlalchemy import Column, String, DateTime, Boolean, Text

from app.models.base import Base


class Project(Base):
    __tablename__ = 'project'

    name = Column(String(255), nullable=False)
    start_date = Column(DateTime, nullable=True)
    is_public = Column(Boolean, default=False)
    description = Column(Text, nullable=False)
    delegate = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(255), nullable=False)
    website = Column(String(255), nullable=True)
