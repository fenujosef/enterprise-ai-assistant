import json

from app.cache.redis_client import redis_client


DEFAULT_TTL = 300


async def get_cached_answer(
    key: str,
):
    value = await redis_client.get(key)

    if value is None:
        return None

    return json.loads(value)


async def cache_answer(
    key: str,
    answer: str,
    ttl: int = DEFAULT_TTL,
):
    await redis_client.setex(
        key,
        ttl,
        json.dumps(answer),
    )