#!/usr/bin/env python3
''' Exercise module '''


from typing import Any, Callable, Union
import redis
import uuid


class Cache:
    ''' Cache class to store and retrieve data '''
    def __init__(self) -> None:
        ''' Initialize the cache '''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' Store data in cache and return a key to retrieve it '''
        data_key = str(uuid.uuid4())
        self._redis = redis.set(data_key, data)
        return data_key


def get(self, key: str, fn: callable = None,) -> Union[str, bytes, int, float]:
    ''' Get data from the cache '''
    data = self._redis.get(key)
    return fn(data) if fn is not None else data


def get_str(self, key: str) -> str:
    ''' Get string from the cache '''
    return self.get(key, lambda x: x.decode('utf-8'))


def get_int(self, key: str) -> int:
    ''' Get integer from the cache '''
    return self.get(key, lambda x: int(x))
