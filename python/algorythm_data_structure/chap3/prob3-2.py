n = int(input())
v = int(input())

count = 0
for _ in range(n):
    if int(input()) == v:
        count += 1

print(count)
