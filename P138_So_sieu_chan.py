#Đề bài
# Số A được gọi là số siêu chẵn được định nghĩa là số được cấu tạochỉ từ các số chẵn.
# Ví dụ: A=4280, A=6666, A=24682468, ….

a = int(input())
so_sieu_chan = True
while a > 0:
    if a % 10 % 2 != 0:
        so_sieu_chan = False
        break
    a //= 10
if so_sieu_chan:
    print("YES")
else:
    print("NO")