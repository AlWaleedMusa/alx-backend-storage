#!/usr/bin/env python3
"a redis class"

import redis
import uuid
from typing import Union

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
