from concurrent.futures import (
    ThreadPoolExecutor,
    Future
)

def func():
    return 1

future = ThreadPoolExecutor().submit(func)
isinstance(future, Future)

print(future.result())
print(future.done())
print(future.running())
print(future.cancelled())