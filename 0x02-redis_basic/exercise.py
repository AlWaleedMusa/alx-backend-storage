#!/usr/bin/env python3
"a redis class"

import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return invoker


class Cache:
    """
    Cache class to interact with a Redis database.

    Methods:
    - __init__: Initializes the Redis connection and flushes the database.
    - store: Stores data in the Redis database with a randomly generated key.
    """

    def __init__(self):
        """
        Initializes the Cache instance.

        - Connects to the Redis database.
        - Flushes the database to remove all existing data.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in the Redis database with a randomly generated key.

        Parameters:
        - data: The data to store, which can be of type str, bytes, int, or float.

        Returns:
        - str: The randomly generated key used to store the data.
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(
        self,
        key: str,
        fn: Callable = None,
    ) -> Union[str, bytes, int, float]:
        """
        Retrieve data from Redis and optionally apply a conversion function.

        Parameters:
        - key: The key to retrieve the data (str).
        - fn: An optional callable to convert the data (Callable).

        Returns:
        - The retrieved data, optionally converted by fn. The data can be of type str, bytes, int, or float.
        - If the key does not exist, it returns None.
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data from Redis and convert it to a string.

        Parameters:
        - key: The key to retrieve the data.

        Returns:
        - The retrieved data as a string.
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data from Redis and convert it to an integer.

        Parameters:
        - key: The key to retrieve the data.

        Returns:
        - The retrieved data as an integer.
        """
        return self.get(key, lambda d: int(d))
