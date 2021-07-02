N: int = int(input("N:"))

a = list()

for i in range(N):
    a.append(int(input("a[%d]" % i)))

min_value: int = 2000000
for i in range(N):
    if min_value > a[i]:
        min_value = a[i]

print(min_value)