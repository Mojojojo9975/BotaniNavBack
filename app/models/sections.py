from sqlalchemy import Column, String, Integer, Float, Boolean
from app.database import Base

class Section(Base):
    __tablename__ = "sections"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    greenhouse_id = Column(Integer, nullable=False)
    is_indoor = Column(Boolean, default=True)
    center_x = Column(Float, nullable=False)
    center_y = Column(Float, nullable=False)
    entry_x = Column(Float, nullable=False)
    entry_y = Column(Float, nullable=False)


class Square(Base):
    __tablename__ = "squares"

    id = Column(String, primary_key=True)
    section_id = Column(String, nullable=False)
    square_number = Column(Integer, nullable=False)
    label = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)