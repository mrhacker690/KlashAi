from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas import HealthResponse
from app.config import settings

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check(db: AsyncSession = Depends(get_db)):
    """
    Health check endpoint.
    """
    # Test database connection
    await db.execute("SELECT 1")

    return HealthResponse(
        status="ok",
        timestamp="2024-01-01T00:00:00Z",  # Replace with actual timestamp logic
        version=settings.APP_VERSION,
    )
