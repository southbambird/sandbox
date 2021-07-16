def chmax(a, b):
    return b if a < b else a

N = int(input("N:"))
W = int(input("W:"))
weight = list()
value  = list()
for i in range(N):
    weight.append(int(input(f"weight[{i}]:")))
    value.append(int(input(f"value[{i}]:")))

dp = [[0 for j in range(W+1)] for i in range(N+1)]

for i in range(N):
    w = 0
    while w <= W:
        if w - weight[i] >= 0:
            dp[i+1][w] = chmax(dp[i+1][w],dp[i][w - weight[i]] + value[i])
        
        dp[i+1][w] = chmax(dp[i+1][w], dp[i][w])
        w = w+1

print(dp[N][W])