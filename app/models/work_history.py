from sqlalchemy import Column, Text, ForeignKey

from app.models import Work
from app.models.base import Base


class WorkHistory(Base):
    __tablename__ = "work_history"

    origin = Column(Text, nullable=True)
    change = Column(Text, nullable=False)
    work_id = Column(ForeignKey(Work.id), nullable=False)
