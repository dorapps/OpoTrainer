from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.user_answer import UserAnswer

def get_user_topic_stats(db: Session, user_id: int):

    results = (
        db.query(
            UserAnswer.topic,
            func.count(UserAnswer.id).label("total"),
            func.sum(UserAnswer.is_correct.cast(Integer)).label("correct")
        )
        .filter(UserAnswer.user_id == user_id)
        .group_by(UserAnswer.topic)
        .all()
    )

    stats = []

    for r in results:

        accuracy = r.correct / r.total if r.total else 0

        if accuracy < 0.4:
            level = "low"
        elif accuracy < 0.7:
            level = "medium"
        else:
            level = "high"

        stats.append({
            "topic": r.topic,
            "accuracy": accuracy,
            "level": level
        })

    return stats