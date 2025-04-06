S = input()
L, R = map(int, input().split())
 
S1 = S[0:L]
S2 = S[L:R]
S3 = S[R:]
result = S2  + S1 + S3

print(result)
