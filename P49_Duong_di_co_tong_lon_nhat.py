n, m = map(int, input().split())
 
dp = [list(map(int, input().split())) for _ in range(n)]
 
for j in range(1, m):
    for i in range(n): 
        lane = dp[i][j-1]
        lane_up = dp[i-1][j-1] if i > 0 else float('-inf')
        lane_down = dp[i+1][j-1] if i < n-1 else float('-inf')
 
        dp[i][j] += max(lane, lane_up, lane_down)
 
print(max(dp[i][m-1] for i in range(n)))
