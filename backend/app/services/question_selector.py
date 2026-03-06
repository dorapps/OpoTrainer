from sqlalchemy.orm import Session
from app.models.question import Question
import random


def get_questions_from_bank(db: Session, topic: str, limit: int = 10):

    questions = (
        db.query(Question)
        .filter(Question.topic == topic)
        .limit(limit)
        .all()
    )

    return questions