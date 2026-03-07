from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Topic(Base):

    __tablename__ = "topics"

    id = Column(Integer, primary_key=True)

    syllabus_id = Column(Integer, ForeignKey("syllabus.id"))

    number = Column(Integer)

    title = Column(String)

    description = Column(String)