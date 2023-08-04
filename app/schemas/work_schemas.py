from datetime import datetime
from typing import Optional

from pydantic import BaseModel, root_validator


class WorkCreate(BaseModel):
    title: str
    description: Optional[str]
    content: str
    due_date: Optional[str]
    assignee_id: Optional[int]

    class Config:
        fields = {
            'due_date': 'dueDate',
            'assignee_id': 'assigneeId'
        }
        allow_population_by_field_name = True

    @root_validator()
    def validate_date(cls, values):
        return values


class WorkResponse(BaseModel):

    id: int
    title: str
    description: Optional[str]
    content: str
    due_date: Optional[datetime]
    created_at: datetime
    updated_at: Optional[datetime]
    status: str
    owner_id: int
    assignee_id: Optional[int]

    class Config:
        fields = {
            'created_at': 'createdAt',
            'updated_at': 'updatedAt',
            'owner_id': 'ownerId',
            'due_date': 'dueDate',
            'assignee_id': 'assigneeId'
        }
        orm_mode = True
        allow_population_by_field_name = True
