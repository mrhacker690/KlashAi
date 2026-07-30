import redis.asyncio as redis

from klashai.config import settings

redis_client: redis.Redis | None = None


async def get_redis() -> redis.Redis:
    """Get Redis client."""
    global redis_client
    if redis_client is None:
        redis_client = redis.from_url(settings.redis_url, decode_responses=True)
    return redis_client
