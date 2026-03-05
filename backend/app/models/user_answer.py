from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.core.database import Base

class UserAnswer(Base):

    __tablename__ = "user_answers"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer)
    question_id = Column(Integer, ForeignKey("questions.id"))

    selected_answer = Column(String)
    is_correct = Column(Boolean)

    topic = Column(String)