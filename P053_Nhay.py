
N, K = map(int, input().split())
buoc_nhay = list(map(int, input().split()))
 
dp = [float('inf')] * N
dp[0] = 0   
 
for i in range(1, N): 
    for k in range(1, K + 1):
        if i - k >= 0:
            dp[i] = min(dp[i], dp[i - k] + abs(buoc_nhay[i] - buoc_nhay[i - k]))
 
print(dp[N - 1])
