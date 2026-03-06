from sqlalchemy.orm import Session
from app.models.question import Question


def save_questions(db: Session, questions):

    saved = []

    for q in questions:

        question = Question(
            text=q["question"],
            option_a=q["options"][0],
            option_b=q["options"][1],
            option_c=q["options"][2],
            option_d=q["options"][3],
            correct_answer=q["correct_answer"],
            topic=q["topic"],
            difficulty=q["difficulty"],
            source="ai"
        )

        db.add(question)
        saved.append(question)

    db.commit()

    return saved