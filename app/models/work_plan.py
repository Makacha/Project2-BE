import enum

from sqlalchemy import Column, ForeignKey, Enum

from app.models.base import Base
from app.models.plan import Plan
from app.models.work import Work


class WorkPlanStatus(enum.Enum):
    INIT = "Khởi tạo"
    RUNNING = "Đang thực hiện"
    DONE = "Hoàn thành"
    PENDING = "Tạm hoãn"


class WorkPlan(Base):
    __tablename__ = 'work_plan'

    work_id = Column(ForeignKey(Work.id), nullable=False)
    plan_id = Column(ForeignKey(Plan.id), nullable=False)
    status = Column(Enum(WorkPlanStatus, values_callable=lambda x: [e.value for e in WorkPlanStatus]), nullable=False,
                    default=WorkPlanStatus.INIT)
