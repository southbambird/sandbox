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

