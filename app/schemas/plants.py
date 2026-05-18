from pydantic import BaseModel, UUID4
from typing import Optional

class PlantBase(BaseModel):
    name: str
    scientific_name: str
    description: Optional[str]
    section: str
    is_indoor: bool

class PlantCreate(PlantBase):
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    greenhouse_id: Optional[str] = None
    indoor_x: Optional[float] = None
    indoor_y: Optional[float] = None

class PlantResponse(PlantBase):
    id: UUID4
    latitude: Optional[float]
    longitude: Optional[float]
    greenhouse_id: Optional[str]

    class Config:
        from_attributes = True