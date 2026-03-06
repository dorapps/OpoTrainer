from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.question import Question
from app.models.user_answer import UserAnswer
from app.services.question_stats import update_question_stats

router = APIRouter()

@router.post("/answer")
def answer_question(
    user_id: int,
    question_id: int,
    selected_answer: str,
    db: Session = Depends(get_db)
):

    question = db.query(Question).get(question_id)

    is_correct = selected_answer == question.correct_answer

    answer = UserAnswer(
        user_id=user_id,
        question_id=question_id,
        selected_answer=selected_answer,
        is_correct=is_correct,
        topic=question.topic
    )

    db.add(answer)

    update_question_stats(db, question_id, is_correct)

    db.commit()

    return {
        "correct": is_correct
    }