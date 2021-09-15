#!/usr/bin/env python3

from functools import lru_cache
from functools import wraps
from datetime import datetime

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = datetime.now()
        result = f(*args, **kw)
        te = datetime.now()
        timediff = te - ts
        print (f'func:{f.__name__} args:[{args}, {kw}] took: {timediff.microseconds} microseconds')
        return result
    return wrap

@lru_cache(maxsize=10)
def fib(number: int) -> int:
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fib(number - 1) + fib(number - 2)

def fib2(number: int) -> int:
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fib2(number - 1) + fib2(number - 2)

@timing
def call_fib_lru(number):
    fib(number)

@timing
def call_fib_non(number):
    fib2(number)

for times in range(10):
    print(f'\n{times} run:')
    call_fib_lru(20+times)
    call_fib_non(20+times)









