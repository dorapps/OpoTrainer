from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.syllabus import SyllabusTopic
from app.services.syllabus.topic_generator import TopicGenerator

router = APIRouter()

generator = TopicGenerator()


@router.post("/syllabus/{topic_id}/generate")
def generate_topic(topic_id: int, db: Session = Depends(get_db)):

    topic = db.query(SyllabusTopic).get(topic_id)

    if not topic:
        return {"error": "Topic not found"}

    content = generator.generate_topic(topic.title)

    topic.content = content
    db.commit()

    return {
        "topic_id": topic.id,
        "status": "generated"
    }