memo = [None] * 50

def fibo(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if memo[n] != None:
        return memo[n]
    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

fibo(49)
for i in range(50):
    print(memo[i])