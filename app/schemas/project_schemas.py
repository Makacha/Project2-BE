from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, root_validator


class ProjectRequest(BaseModel):
    project_id: int
    role: Optional[str]

    class Config:
        fields = {
            'project_id': 'projectId'
        }
        allow_population_by_field_name = True


class ProjectCreate(BaseModel):
    name: str
    is_public: Optional[bool] = None
    start_date: Optional[str] = None
    categories: Optional[List[str]]
    description: str
    delegate: str
    phone: str
    email: str
    website: Optional[str]

    class Config:
        fields = {'is_public': 'isPublic',
                  'start_date': 'startDate'}
        allow_population_by_field_name = True

    @root_validator
    def validate_data(cls, data):
        if data.get("start_date") is None:
            data["start_date"] = datetime.now().strftime("%d/%m/%Y")
        if data.get("is_public") is None:
            data["is_public"] = True
        return data


class ProjectResponse(BaseModel):
    id: int
    name: str
    is_public: Optional[bool]
    start_date: Optional[datetime]
    categories: Optional[List[str]]
    description: str
    delegate: str
    phone: str
    email: str
    website: Optional[str]
    role: Optional[str]
    member_status: Optional[str]

    class Config:
        fields = {"is_public": "isPublic",
                  "start_date": "startDate",
                  "member_status": "memberStatus"}
        orm_mode = True
        allow_population_by_field_name = True
