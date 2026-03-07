from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    statement = Column(Text, nullable=False)

    option_a = Column(String(255), nullable=False)
    option_b = Column(String(255), nullable=False)
    option_c = Column(String(255), nullable=False)
    option_d = Column(String(255), nullable=False)

    correct_answer = Column(String(1), nullable=False)
    topic = Column(String)
    difficulty = Column(String)
    exam_id = Column(Integer, ForeignKey("exams.id"))
    source = Column(String)  # ai | exam_real

    exam = relationship("Exam", back_populates="questions")
    topic_id = Column(Integer, ForeignKey("topics.id"))