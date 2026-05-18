from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models.plant import Plant
from app.schemas.navigation import OutdoorRouteRequest, OutdoorRouteResponse
from app.services.navigation import get_outdoor_route, get_indoor_route
from app.core.auth import verify_api_key

router = APIRouter(prefix="/navigation", tags=["navigation"])

@router.post("/route", response_model=OutdoorRouteResponse)
async def get_route(
    request: OutdoorRouteRequest,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(verify_api_key)
):
    result = await db.execute(select(Plant).where(Plant.id == request.plant_id))
    plant = result.scalar_one_or_none()
    if not plant:
        raise HTTPException(status_code=404, detail="Plant not found")

    if plant.is_indoor:
        # Returns 501 until phase 3
        raise HTTPException(status_code=501, detail="Indoor navigation not yet available")

    if not plant.latitude or not plant.longitude:
        raise HTTPException(status_code=400, detail="Plant has no outdoor coordinates")

    return await get_outdoor_route(request.user_latitude, request.user_longitude, plant)