from sqlalchemy.orm import Session
from app.models.question_stats import QuestionStats


def update_question_stats(db: Session, question_id: int, is_correct: bool):

    stats = (
        db.query(QuestionStats)
        .filter(QuestionStats.question_id == question_id)
        .first()
    )

    if not stats:

        stats = QuestionStats(
            question_id=question_id,
            total_answers=0,
            correct_answers=0
        )

        db.add(stats)

    stats.total_answers += 1

    if is_correct:
        stats.correct_answers += 1

    stats.success_rate = stats.correct_answers / stats.total_answers

    db.commit()