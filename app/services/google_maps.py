import httpx
from app.config import settings

DIRECTIONS_URL = "https://maps.googleapis.com/maps/api/directions/json"

async def get_walking_directions(
    origin_lat: float,
    origin_lng: float,
    dest_lat: float,
    dest_lng: float
) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(DIRECTIONS_URL, params={
            "origin": f"{origin_lat},{origin_lng}",
            "destination": f"{dest_lat},{dest_lng}",
            "mode": "walking",
            "key": settings.google_maps_api_key
        })
        data = response.json()

        if data["status"] != "OK":
            raise ValueError(f"Google Maps error: {data['status']}")

        leg = data["routes"][0]["legs"][0]
        return {
            "distance_metres": leg["distance"]["value"],
            "duration_seconds": leg["duration"]["value"],
            "polyline": data["routes"][0]["overview_polyline"]["points"],
            "steps": leg["steps"]
        }