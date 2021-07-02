N = int(input("N:"))
K = int(input("K:"))
a = list()
b = list()

for i in range(N):
    a.append(int(input("a[%d]" % i)))

for i in range(N):
    b.append(int(input("b[%d]" % i)))

min: int = 20000000

for a_i in range(N):
    for b_i in range(N):
        value = a[a_i] + b[b_i]
        if value < K:
            continue
        if value < min:
            min = value

print(min)