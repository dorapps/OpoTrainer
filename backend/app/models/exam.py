from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy.orm import relationship

class Exam(Base):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    year = Column(Integer, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    questions = relationship("Question", back_populates="exam", cascade="all, delete")
    
    name = Column(String)
    organization = Column(String)
    level = Column(String)