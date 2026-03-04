from pydantic import BaseModel
from typing import List


class QuestionBase(BaseModel):
    statement: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: str


class QuestionCreate(QuestionBase):
    exam_id: int


class QuestionResponse(QuestionBase):
    id: int
    exam_id: int

    class Config:
        from_attributes = True