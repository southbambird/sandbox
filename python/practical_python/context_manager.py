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