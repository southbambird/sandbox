with open('some.txt', 'w') as f:
    f.write('python')

print(f.closed)

class ContextManager:
    def __enter__(self):
        print('__enter__ was called')
    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__ was called')
        print(f'{exc_type}')
        print(f'{exc_value}')
        print(f'{traceback}')

with ContextManager():
    print('inside the block')

#with ContextManager():
#    1 / 0

class ContextManager2:
    def __enter__(self):
        return 1
    def __exit__(self, exc_type, exc_value, traceback):
        pass

with ContextManager2() as f:
    print(f)

class Point:
    def __init__(self, **kwargs):
        self.value = kwargs
    def __enter__(self):
        print('__enter__ was called')
        return self.value
    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__ was called')
        print(self.value)

with Point(x=1, y=2) as p:
    print(p)
    p['z'] = 3

from contextlib import contextmanager
@contextmanager
def point(**kwargs):
    print('__enter__ was called')
    value = kwargs
    try:
        yield value
    except Exception as e:
        print(e)
        raise
    finally:
        print('__exit__ was called')
        print(value)

with point(x=1, y=2) as p:
    print(p)
    p['z'] = 3