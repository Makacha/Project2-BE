from datetime import datetime
from typing import Optional

from pydantic import BaseModel, root_validator


class DocumentCreate(BaseModel):
    title: str
    description: Optional[str]
    content: str

    @root_validator()
    def validate_date(cls, values):
        return values


class DocumentResponse(BaseModel):

    id: int
    title: str
    description: Optional[str]
    content: str
    created_at: datetime
    updated_at: Optional[datetime]
    status: str
    owner_id: int

    class Config:
        fields = {
            'created_at': 'createdAt',
            'updated_at': 'updatedAt',
            'owner_id': 'ownerId'
        }
        orm_mode = True
        allow_population_by_field_name = True
