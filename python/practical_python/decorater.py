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
