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

apple.price = 256
