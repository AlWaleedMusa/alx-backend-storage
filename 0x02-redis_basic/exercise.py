#!/usr/bin/env python3
"a redis class"

import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of calls to a method.

    Parameters:
    - method: The method to be decorated (Callable).

    Returns:
    - Callable: The decorated method that increments the call count each time it is invoked.
    """

    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """
        Wrapper function that increments the call count and then calls the original method.

        Parameters:
        - self: The instance of the class.
        - *args: Positional arguments to pass to the method.
        - **kwargs: Keyword arguments to pass to the method.

        Returns:
        - Any: The result of the original method call.
        """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return invoker


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a method in Redis.

    Parameters:
    - method: The method to be decorated (Callable).

    Returns:
    - Callable: The decorated method that logs its inputs and outputs to Redis.
    """

    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """
        Wrapper function that logs the inputs and outputs of the method to Redis.

        Parameters:
        - self: The instance of the class.
        - *args: Positional arguments to pass to the method.
        - **kwargs: Keyword arguments to pass to the method.

        Returns:
        - Any: The result of the original method call.
        """
        in_key = "{}:inputs".format(method.__qualname__)
        out_key = "{}:outputs".format(method.__qualname__)

        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))

        output = method(self, *args, **kwargs)

        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, output)

        return output

    return invoker


def replay(fn: Callable) -> None:
    """Displays the call history of a Cache class' method"""

    if fn is None or not hasattr(fn, "__self__"):
        return

    redis_store = getattr(fn.__self__, "_redis", None)
    if not isinstance(redis_store, redis.Redis):
        return

    fxn_name = fn.__qualname__
    in_key = "{}:inputs".format(fxn_name)
    out_key = "{}:outputs".format(fxn_name)
    fxn_call_count = 0

    if redis_store.exists(fxn_name) != 0:
        fxn_call_count = int(redis_store.get(fxn_name))

    print("{} was called {} times:".format(fxn_name, fxn_call_count))
    fxn_inputs = redis_store.lrange(in_key, 0, -1)
    fxn_outputs = redis_store.lrange(out_key, 0, -1)

    for fxn_input, fxn_output in zip(fxn_inputs, fxn_outputs):
        print(
            "{}(*{}) -> {}".format(
                fxn_name,
                fxn_input.decode("utf-8"),
                fxn_output,
            )
        )


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

    @call_history
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
