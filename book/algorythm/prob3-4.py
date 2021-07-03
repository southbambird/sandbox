N: int = int(input("N:"))

a = list()

for i in range(N):
    a.append(int(input("a[%d]" % i)))

max: int = -2000000
for i in range(N):
    for j in range(i+1,N):
        if max < abs(a[i] - a[j]):
            max = abs(a[i] - a[j])

print(max)