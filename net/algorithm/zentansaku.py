def integer_to_vector(bit, n):
    vec = []
    for i in range(n):
        if bit & (1 << i):
            vec.append(i)
    return vec

a = list(map(int, input().split(' ')))
w = int(input())
finded = False
for i in range(1 << len(a)):
    vec = integer_to_vector(i, len(a))
    print(vec)
    sum = 0
    for i in vec:
        sum += a[i]
    if sum == w:
        finded = True

if finded:
    print("Yes.")
else:
    print("No.")