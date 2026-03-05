from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.exam import Exam
from app.schemas.exam import ExamCreate, ExamResponse
from app.services.ai_generator import generate_adaptive_questions

router = APIRouter(prefix="/exams", tags=["Exams"])


@router.post("/", response_model=ExamResponse)
def create_exam(exam: ExamCreate, db: Session = Depends(get_db)):
    db_exam = Exam(**exam.model_dump())
    db.add(db_exam)
    db.commit()
    db.refresh(db_exam)
    return db_exam


@router.get("/", response_model=List[ExamResponse])
def list_exams(db: Session = Depends(get_db)):
    return db.query(Exam).all()

@router.post("/adaptive-exam/{user_id}")
def create_adaptive_exam(user_id: int, db: Session = Depends(get_db)):

    questions = generate_adaptive_questions(db, user_id)

    return {
        "questions": questions
    }