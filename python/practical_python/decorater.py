from functools import lru_cache
from time import sleep
@lru_cache(maxsize=32)
def heavy_function(n):
#    sleep(3)
    return n+1

print(heavy_function(2))

print(heavy_function(2))

from dataclasses import dataclass

@dataclass(frozen=True)
class Fruit:
    name: str
    price: int = 0

apple = Fruit(name='apple', price=128)
print(apple)

#apple.price = 256


def deco1(f):
    print('deco1 called')
    def wrapper():
        print('before exec')
        v = f()
        print('after exec')
        return v
    return wrapper

@deco1
def func():
    print('exec')
    return 1

print(func.__name__)

print(func())

def deco2(f):
    def wrapper(*args, **kwargs):
        print('before exec')
        v = f(*args, **kwargs)
        print('after exec')
        return v
    return wrapper

@deco2
def func2(x, y):
    print('exec')
    return x, y

print(func2(1, 2))

def deco3(z):
    def _deco3(f):
        def wrapper(*args, **kwargs):
            print('before exec3', z)
            v = f(*args, **kwargs)
            print('after exec3', z)
            return v
        return wrapper
    return _deco3

@deco3(z=3)
def func3(x, y):
    print('exec3')
    return x,y

print(func3(1, 2))


from functools import wraps
def deco4(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('before exec')
        v = f(*args, **kwargs)
        print('after exec')
        return v
    return wrapper

@deco4
def func4():
    '''func4です'''
    print('exec')

print(func4.__name__)
print(func4.__doc__)


import time
def elapsed_time(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        v = f(*args, *kwargs)
        print(f"{f.__name__}: {time.time() - start}")
        return v
    return wrapper

@elapsed_time
def func5(n):
    return sum(i for i in range(n))

print(f'{func5(100000)}')

