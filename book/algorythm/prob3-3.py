N: int = int(input("N:"))

a = list()

for i in range(N):
    a.append(int(input("a[%d]" % i)))

first_min: int = 2000000
for i in range(N):
    if first_min > a[i]:
        first_min = a[i]

second_min: int = 2000000
for i in range(N):
    if a[i] == first_min:
        continue
    if second_min > a[i]:
        second_min = a[i]

print(first_min)
print(second_min)