import redis
from loguru import logger

from end_point.cfg import REDIS_HOST, REDIS_PORT, CACHE_ACTIVE


class Cache:
    """
        Fake in-memory cache
    """
    def __init__(self):
        self.data = {}

    def get(self, key: str) -> str:
        return  self.data.get(key)

    def set(self, key: dict, value: str):
        self.data[key] = value

# json.dumps(sample)
def cache():
    if CACHE_ACTIVE:
        try:
            c = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        except Exception:
            c = Cache()
            logger.error("Conection error cache server")
    else:
        c = Cache()
    return c


redis_db = cache()




