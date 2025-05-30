#Cho hai chuoi, tim do dai xau con chung dai nhat giua hai xau code sai 
# s1 = input()
# s2 = input()

# n, m = len(s1), len(s2)
# dp = [[0] * (m + 1) for _ in range(n + 1)]

# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         if s1[i - 1] == s2[j - 1]:
#             dp[i][j] = dp[i - 1][j - 1] + 1
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# print(dp[n][m])

#code đúng
s1 = input().strip()
s2 = input().strip()

n, m = len(s1), len(s2)
 
p = [0] * (m + 1)
c = [0] * (m + 1)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
            c[j] = p[j - 1] + 1
        else:
            c[j] = max(p[j], c[j - 1]) 
    p, c = c, p

print(p[m])