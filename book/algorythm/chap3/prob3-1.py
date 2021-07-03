N = int(input("N:"))
v = int(input("v:"))

a = list()

for i in range(N):
    a.append(int(input("a[%d]" % i)))

count_i: int = -1

for i in range(N):
    if(a[i] == v):
        count_i = i

print(count_i)

