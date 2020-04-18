def inf(n):
    while True:
        yield n

#for i in inf(3):
#    print(i)

def gen_function(n):
    print('start')
    while n:
        print(f'yield: {n}')
        yield n
        n -= 1

gen = gen_function(2)

next(gen)
next(gen)
#next(gen)

for i in gen_function(2):
    print(i)

print([i for i in gen_function(5)])
print(max(gen_function(5)))

x = [1, 2, 3, 4, 5]
gen = (i**2 for i in x)
print(list(gen))


def chain(iterables):
    for iterable in iterables:
        for v in iterable:
            yield v

iterables = ('python', 'book')
print(list(chain(iterables)))

def chain2(iterables):
    for iterable in iterables:
        yield from (v for v in iterable)

print(list(chain2(iterables)))