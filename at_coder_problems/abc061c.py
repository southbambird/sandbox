s = input()
n = len(s)
for bit in range(1 << n):
    for i in range(n):
        if((bit >> i) & 1):
