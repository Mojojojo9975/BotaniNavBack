from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models.plant import Plant
from app.schemas.plant import PlantResponse, PlantCreate
from app.core.auth import verify_api_key

router = APIRouter(prefix="/plants", tags=["plants"])

@router.get("/", response_model=list[PlantResponse])
async def list_plants(
    is_indoor: bool | None = None,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(verify_api_key)
):
    query = select(Plant)
    if is_indoor is not None:
        query = query.where(Plant.is_indoor == is_indoor)
    result = await db.execute(query)
    return result.scalars().all()

@router.get("/{plant_id}", response_model=PlantResponse)
async def get_plant(
    plant_id: str,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(verify_api_key)
):
    result = await db.execute(select(Plant).where(Plant.id == plant_id))
    plant = result.scalar_one_or_none()
    if not plant:
        raise HTTPException(status_code=404, detail="Plant not found")
    return plant

@router.post("/", response_model=PlantResponse)
async def create_plant(
    plant_data: PlantCreate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(verify_api_key)
):
    plant = Plant(**plant_data.model_dump())
    db.add(plant)
    await db.commit()
    await db.refresh(plant)
    return plant