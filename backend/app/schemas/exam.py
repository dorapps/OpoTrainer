from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from typing import List
from app.schemas.question import QuestionResponse

class ExamBase(BaseModel):
    title: str
    description: Optional[str] = None
    year: Optional[int] = None


class ExamCreate(ExamBase):
    pass


class ExamResponse(ExamBase):
    id: int
    created_at: datetime
    questions: List[QuestionResponse] = []

    class Config:
        from_attributes = True  # importante para SQLAlchemy 2