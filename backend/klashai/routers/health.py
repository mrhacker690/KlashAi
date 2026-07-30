from fastapi import APIRouter

from klashai.services.health import HealthService

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    return await HealthService.check()
