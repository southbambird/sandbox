x = [1, 2, 3]
y = [4, 5, 6]

zip(x, y)

print(list(zip(x, y)))


x = [1, 2, 3]
y = [4, 5, 6, 7]
z = [8, 9]

print(list(zip(x, y ,z)))

from itertools import zip_longest
print(list(zip_longest(x, y, z, fillvalue=0)))



x = [1, 4, 3, 5, 2]
y = [1, 4, 3, 5, 2]

x.sort()
print(x)

print(sorted(y))
print(y)

print(sorted(y, reverse=True))

x = ['1','4', 3, 1, '1']
sorted(x, key=lambda v: int(v))




x = (1, 4, 3, 5, 2)
print(list(filter(lambda i: i > 3, x)))




