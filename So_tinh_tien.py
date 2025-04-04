#Kiểm tra Số tịnh tiến một đơn vị
n = int(input())
s = str(n)

so_tinh_tien= True

for i in range(len(s)-1):
    if abs(int(s[i]) - int(s[i+1])) != 1:
        so_tinh_tien = False
        break

if so_tinh_tien:
    print("YES")
else:
    print("NO")