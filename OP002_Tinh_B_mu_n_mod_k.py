
B,n,k = map(int, input().split())
S = (B**n) % k
print(S)

B,n,k = map(int, input().split())
S = pow(B, n, k)
print(S)
