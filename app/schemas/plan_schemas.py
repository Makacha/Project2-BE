from datetime import datetime
from typing import Optional

from pydantic import BaseModel, root_validator


class PlanCreate(BaseModel):
    title: str
    description: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]

    class Config:
        fields = {
            'start_date': 'startDate',
            'end_date': 'endDate'
        }
        allow_population_by_field_name = True

    @root_validator()
    def validate_date(cls, values):
        return values


class PlanResponse(BaseModel):

    id: int
    title: str
    description: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]
    start_date: Optional[datetime]
    end_date: Optional[datetime]

    class Config:
        fields = {
            'created_at': 'createdAt',
            'updated_at': 'updatedAt',
            'start_date': 'startDate',
            'end_date': 'endDate'
        }
        orm_mode = True
        allow_population_by_field_name = True
