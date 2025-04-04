##Tính tổng hàng với cột trong ma trận nhập vào từ bàn phím
m, n = map(int, input().split())

a = []
for i in range(m): 
    a.append(list(map(int, input().split())))

tong = 0

for i in range(m):
    for j in range(n):
        tong += a[i][j] if i == 1 or j == 1 else 0
print(tong)