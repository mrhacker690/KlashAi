from datetime import datetime

from klashai.schemas.health import HealthResponse


class HealthService:
    @staticmethod
    async def check() -> HealthResponse:
        return HealthResponse(
            status="ok",
            timestamp=datetime.utcnow().isoformat(),
            version="0.1.0",
        )
