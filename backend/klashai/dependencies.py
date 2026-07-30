from fastapi import Depends

from klashai.core.database import get_db
from klashai.core.redis import get_redis


async def get_db_session():
    """Dependency for database session."""
    return Depends(get_db)


async def get_redis_client():
    """Dependency for Redis client."""
    return Depends(get_redis)
