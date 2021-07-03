K: int = int(input("K:"))
N: int = int(input("N:"))

count = 0
for x in range(K):
    for y in range(K):
        z = N - x - y
        if 0 <= z & z <= K:
            count = count + 1

print(count)