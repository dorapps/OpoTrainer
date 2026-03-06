from sqlalchemy import Column, Integer, Float, ForeignKey
from app.core.database import Base

class QuestionStats(Base):

    __tablename__ = "question_stats"

    id = Column(Integer, primary_key=True)

    question_id = Column(Integer, ForeignKey("questions.id"))

    total_answers = Column(Integer, default=0)

    correct_answers = Column(Integer, default=0)

    success_rate = Column(Float, default=0)