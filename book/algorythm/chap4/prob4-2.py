memo = [None] * 100

def func(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    if memo[n]:
        return memo[n]
    else:
        memo[n] = func(n-1) + func(n-2) + func(n-3)
        return memo[n]

N = int(input("N:"))
for i in range(N):
    print(func(i))