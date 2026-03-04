from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ExamBase(BaseModel):
    title: str
    description: Optional[str] = None
    year: Optional[int] = None


class ExamCreate(ExamBase):
    pass


class ExamResponse(ExamBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # importante para SQLAlchemy 2