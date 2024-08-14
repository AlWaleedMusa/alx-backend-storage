#!/usr/bin/env python3
"""A module for request caching and tracking.""""

from functools import wraps
import redis
import requests
from typing import Callable


redis_store = redis.Redis()


def data_cache(method: Callable) -> Callable:
    """
    Decorator to cache the output of fetched data.

    Increments the request count for the URL and caches the result for 10 seconds.
    """
    @wraps(method)
    def invoker(url: str) -> str:
        """
        Wrapper function to handle caching and request counting.
        
        Parameters:
        - url: The URL to fetch data from (str).
        
        Returns:
        - str: The content of the URL.
        """
        redis_store.incr(f"count:{url}")
        result = redis_store.get(f"result:{url}")
        if result:
            return result.decode("utf-8")
        result = method(url)
        redis_store.set(f"count:{url}", 0)
        redis_store.setex(f"result:{url}", 10, result)
        return result

    return invoker

@data_cache
def get_page(url: str) -> str:
    """
    Fetches the content of a URL and caches the response.
    
    Parameters:
    - url: The URL to fetch data from (str).
    
    Returns:
    - str: The content of the URL.
    """
    return requests.get(url).text
