# Nhập dữ liệu ??????????
n,W = map(int,input().split())

weights = []
values = []
 
for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)
 
dp = [[0] * (W + 1) for _ in range(n + 1)]
 
for i in range(1, n + 1):
    for w in range(W + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
        else:
            dp[i][w] = dp[i - 1][w]
 
print(dp[n][W])
