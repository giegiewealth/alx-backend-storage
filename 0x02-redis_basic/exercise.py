import redis
import uuid
from typing import Union, Callable
from functools import wraps
import functools

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()
        self._call_counts = {}

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
@@ -38,3 +29,11 @@ def get_str(self, key: str) -> Union[str, bytes, None]:

    def get_int(self, key: str) -> Union[int, None]:
        return self.get(key, fn=int)

def count_calls(method: Callable) -> Callable:
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._call_counts[key] = self._call_counts.get(key, 0) + 1
        return method(self, *args, **kwargs)
    return wrapper
