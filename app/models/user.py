from sqlalchemy import Column, String

from app.models.base import Base


class User(Base):
    __tablename__ = 'user'

    username = Column(String(255), nullable=False, unique=True)
    fullname = Column(String(255), nullable=True)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone = Column(String(20), nullable=True)
