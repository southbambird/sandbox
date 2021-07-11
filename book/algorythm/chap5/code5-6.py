def chmin(a, b):
    if a > b:
        return b
    else:
        return a

INF = 1 << 60

def rec(i: int):
    if(dp[i] < INF):
        return dp[i]
    
    if i == 0:
        return 0

    res = INF

    res = chmin(res, rec(i-1) + abs(h[i] - h[i-1]))
    print("res" + str(res))
    if i > 1:
        res = chmin(res, rec(i-2) + abs(h[i] - h[i-2]))
    
    dp[i] = res
    return dp[i]

N: int = int(input("N:"))
h = list()
dp = [INF] * N
for i in range(N):
    h.append(int(input("h[%d]:" % i)))

print(rec(N-1))