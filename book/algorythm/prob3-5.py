N: int = int(input("N:"))

a = list()

for i in range(N):
    a.append(int(input("a[%d]" % i)))

for count in range(200000):
    for i in range(N):
        if a[i] % 2 == 0:
            a[i] = a[i] / 2
        else:
            break
    else:
        continue
    break

print(count)