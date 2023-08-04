import enum

from sqlalchemy import Column, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship

from app.models import User
from app.models.base import Base
from app.models.project import Project


class MemberRole(enum.Enum):
    OWNER = "Chủ dự án"
    ADMIN = "Quản trị viên"
    MEMBER = "Thành viên"
    GUEST = "Khách"


class MemberStatus(enum.Enum):
    WAITING = "Chờ duyệt"
    ACTIVE = "Đang tham gia"
    INACTIVE = "Ngừng tham gia"


class Member(Base):
    __tablename__ = "member"

    project_id = Column(ForeignKey(Project.id), nullable=False)
    project = relationship(Project)
    user_id = Column(ForeignKey(User.id), nullable=False)
    user = relationship(User)
    role = Column(Enum(MemberRole, values_callable=lambda x: [e.value for e in MemberRole]),
                  nullable=False, default=MemberRole.GUEST)
    join_date = Column(DateTime, nullable=False)
    status = Column(Enum(MemberStatus, values_callable=lambda x: [e.value for e in MemberStatus]),
                    nullable=False, default=MemberStatus.WAITING)
