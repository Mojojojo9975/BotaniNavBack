from fastapi import FastAPI
from app.routers import plants, navigation
from app.core.errors import register_error_handlers

app = FastAPI(
    title="Botanical Navigation API",
    version="1.0.0",
    description="Navigation API for botanical garden visitor app"
)

app.include_router(plants.router, prefix="/api/v1")
app.include_router(navigation.router, prefix="/api/v1")

register_error_handlers(app)

@app.get("/health")
async def health():
    return {"status": "ok", "version": "1.0.0"}