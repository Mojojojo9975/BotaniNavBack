from pydantic import BaseModel
from typing import Optional
from enum import Enum

class NavigationMode(str, Enum):
    outdoor = "outdoor"
    indoor = "indoor"

class OutdoorRouteRequest(BaseModel):
    user_latitude: float
    user_longitude: float
    plant_id: str

class OutdoorRouteResponse(BaseModel):
    mode: NavigationMode = NavigationMode.outdoor
    plant_name: str
    distance_metres: float
    duration_seconds: int
    polyline: str          # encoded Google Maps polyline
    destination_lat: float
    destination_lng: float
    steps: list[dict]