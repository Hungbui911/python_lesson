#Cho một số tự nhiên X, hãy kiểm tra xem X có thể tách thành tổng của 2 hay nhiều số tự nhiên liên tiếp không?
n = int(input())

for k in range(2, int((2 * n) ** 0.5) + 1): 
    if (n - k * (k - 1) // 2) % k == 0:
        print("YES")
        break
else:
    print("NO")