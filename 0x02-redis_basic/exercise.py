#!/usr/bin/env python3
''' Exercise module '''


from typing import Any, Callable, Union
import redis
import uuid


class Cache:
    def __init__(self) -> None:
        ''' Initialize the cache '''
        self._redis = redis.Redis()
        self._redis.flushdb(True)
 
    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' Store data in cache and return a key to retrieve it '''
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key
