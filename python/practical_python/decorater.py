from functools import lru_cache
from time import sleep
@lru_cache(maxsize=32)
def heavy_function(n):
    sleep(3)
    return n+1

print(heavy_function(2))

print(heavy_function(2))