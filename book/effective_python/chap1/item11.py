a = ['a', 'b', 'c', 'd', 'e', 'e', 'f', 'g', 'h']

print('Before', a)
a[2:7] = [99, 22, 14]
print('After ', a)

b = a[:]
assert b == a and b is not a

b = a
print('Before a', a)
print('Before b', b)

a[:] = [101, 102, 103]
assert a is b
print('After a', a)
print('After b', b)

