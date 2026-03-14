import json
from pathlib import Path

from app.core.database import SessionLocal
from app.models.exam import Exam
from app.models.syllabus import Syllabus
from app.models.topic import Topic


DATA_PATH = Path("data/syllabus")


def import_file(file_path):

    db = SessionLocal()

    with open(file_path) as f:
        data = json.load(f)

    exam_data = data["exam"]
    syllabus_data = data["syllabus"]
    topics = data["topics"]

    exam = Exam(**exam_data)

    db.add(exam)
    db.commit()
    db.refresh(exam)

    syllabus = Syllabus(
        exam_id=exam.id,
        version=syllabus_data["version"]
    )

    db.add(syllabus)
    db.commit()
    db.refresh(syllabus)

    for topic in topics:

        db_topic = Topic(
            syllabus_id=syllabus.id,
            number=topic["number"],
            title=topic["title"]
        )

        db.add(db_topic)

    db.commit()

    print(f"Syllabus imported: {exam.name}")


def seed_all():

    for file in DATA_PATH.glob("*.json"):

        import_file(file)


if __name__ == "__main__":
    seed_all()