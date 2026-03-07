from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Syllabus(Base):

    __tablename__ = "syllabus"

    id = Column(Integer, primary_key=True)

    exam_id = Column(Integer, ForeignKey("exams.id"))

    version = Column(String)