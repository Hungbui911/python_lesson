#Tính tổng ở vị trí lẻ trong mảng
n = int(input())
mang = []
for _ in range(n):
    x = int(input())
    mang.append(x) 

tong = 0
for i in range(1,n,2):
    tong += mang[i]

print(tong)
