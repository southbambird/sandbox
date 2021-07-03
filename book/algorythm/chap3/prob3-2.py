N = int(input("N:"))
v = int(input("v:"))

a = list()

for i in range(N):
    a.append(int(input("a[%d]" % i)))

count: int = 0

for i in range(N):
    if(a[i] == v):
        count = count + 1

print(count)