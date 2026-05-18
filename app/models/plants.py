from sqlalchemy import Column, String, Boolean, Float, Text
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
import uuid

class Plant(Base):
    __tablename__ = "plants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    scientific_name = Column(String, nullable=False)
    description = Column(Text)
    section = Column(String, nullable=False)
    is_indoor = Column(Boolean, default=False)

    # Outdoor plants — real GPS coordinates
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    # Indoor plants — greenhouse local coordinates
    # These stay null until DXF and hardware are ready
    greenhouse_id = Column(String, nullable=True)
    indoor_x = Column(Float, nullable=True)
    indoor_y = Column(Float, nullable=True)