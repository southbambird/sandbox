n = int(input())
mochi = []

for i in range(n):
    mochi.append(int(input()))

mochi_kai = sorted(list(set(mochi)))

print(len(mochi_kai))