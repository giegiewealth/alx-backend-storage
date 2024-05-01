import redis
import uuid
from typing import Union, Callable
from typing import Callable
from functools import wraps

class Cache:
@@ -19,7 +19,27 @@ def wrapper(self, *args, **kwargs):
            return method(self, *args, **kwargs)
        return wrapper
