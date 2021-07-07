def chmin(a, b):
    if a > b:
        a = b

INF = 1 << 60

N = int(input("N:"))
h = list()
for i in range(N):
    h.append(int(input("h[%d]:" % i)))

dp = [INF] * N

dp[0] = 0

for i in range(1, N):
    chmin(dp[i], dp[i-1] + abs(h[i] - h[i-1]))
    if i > 1:
        chmin(dp[i], dp[i-2] + abs(h[i] - h[i-2]))


print(dp)
print(INF)