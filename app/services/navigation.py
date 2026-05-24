from app.services.google_maps import get_walking_directions
from app.models.plant import Plant
from app.schemas.navigation import OutdoorRouteResponse, NavigationMode

async def get_outdoor_route(
    user_lat: float,
    user_lng: float,
    plant: Plant
) -> OutdoorRouteResponse:
    directions = await get_walking_directions(
        user_lat, user_lng,
        plant.latitude, plant.longitude
    )
    return OutdoorRouteResponse(
        mode=NavigationMode.outdoor,
        plant_name=plant.name,
        destination_lat=plant.latitude,
        destination_lng=plant.longitude,
        **directions
    )

async def get_indoor_route(user_position: dict, plant: Plant):
    # Placeholder — implemented when DXF and hardware are ready
    raise NotImplementedError("Indoor navigation coming in phase 3")