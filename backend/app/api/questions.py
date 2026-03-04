from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.question import Question
from app.models.exam import Exam
from app.schemas.question import QuestionCreate, QuestionResponse

router = APIRouter(prefix="/questions", tags=["Questions"])


@router.post("/", response_model=QuestionResponse)
def create_question(question: QuestionCreate, db: Session = Depends(get_db)):

    exam = db.query(Exam).filter(Exam.id == question.exam_id).first()
    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")

    db_question = Question(**question.model_dump())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    return db_question


@router.get("/exam/{exam_id}", response_model=List[QuestionResponse])
def get_exam_questions(exam_id: int, db: Session = Depends(get_db)):
    return db.query(Question).filter(Question.exam_id == exam_id).all()