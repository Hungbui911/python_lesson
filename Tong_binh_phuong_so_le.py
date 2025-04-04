#Tính tổng bình phương số lẻ S= 1^2 + 3^2 + 5^2 + ... + (2*n+1)^2
n = int(input())
S = sum((2*i+1)**2 for i in range(n+1))
print(S)