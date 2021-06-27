n = int(input())
a = []
for _ in range(n):
    hints = []
    for _ in range(int(input())):
        hints.append((*list(map(int,input().split(' ')))))
    a.append(hints)

print(len(a))
