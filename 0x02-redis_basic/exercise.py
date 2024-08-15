#!/usr/bin/env python3
''' Exercise module '''


import redis
import uuid
from functools import wraps
from typing import Any, Callable, Union


def count_calls(method: Callable) -> Callable:
    ''' Count the number of calls to a method '''
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        ''' Method invoker '''
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoker


def call_history(method: Callable) -> Callable:
    ''' Store the history of inputs and outputs '''
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        ''' Method invoker '''
        in_key = '{}:inputs'.format(method.__qualname__)
        out_key = '{}:outputs'.format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, output)
        return output
    return invoker


def replay(fn: Callable) -> None:
    ''' Display the history of calls '''
    if fn is None or not hasattr(fn, '__self__'):
        return
    redis_store = getattr(fn.__self__, '_redis', None)
    if not isinstance(redis_store, redis.Redis):
        return
    fxn_name = fn.__qualname__
    in_key = '{}:inputs'.format(fxn_name)
    out_key = '{}:outputs'.format(fxn_name)
    fxn_call_count = 0
    if redis_store.exists(fxn_name) != 0:
        fxn_call_count = int(redis_store.get(fxn_name))
    print('{} was called {} times:'.format(fxn_name, fxn_call_count))
    fxn_inputs = redis_store.lrange(in_key, 0, -1)
    fxn_outputs = redis_store.lrange(out_key, 0, -1)
    for fxn_input, fxn_output in zip(fxn_inputs, fxn_outputs):
        print('{}(*{}) -> {}'.format(
            fxn_name,
            fxn_input.decode("utf-8"),
            fxn_output,
        ))


class Cache:
    ''' Cache class to store and retrieve data '''

    def __init__(self) -> None:
        ''' Initialize the cache '''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' Store data in cache and return a key to retrieve it '''
        data_key = str(uuid.uuid4())
        self._redis = redis.set(data_key, data)
        return data_key


def get(self, key: str, fn: Callable = None,) -> Union[str, bytes, int, float]:
    ''' Get data from the cache '''
    data = self._redis.get(key)
    return fn(data) if fn is not None else data


def get_str(self, key: str) -> str:
    ''' Get string from the cache '''
    return self.get(key, lambda x: x.decode('utf-8'))


def get_int(self, key: str) -> int:
    ''' Get integer from the cache '''
    return self.get(key, lambda x: int(x))
