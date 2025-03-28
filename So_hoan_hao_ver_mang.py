# Bài nói về số hoàn hảo nhưng mà là cần nhập vào là mảng chứ k phải 1 số nữa
# Đọc số lượng phần tử
n = int(input())
a = [int(input()) for _ in range(n)]
ds_so_hoan_hao = []
for so_hoan_hao in a:
    if so_hoan_hao < 2:
        continue   
    t = 1  
    for i in range(2, so_hoan_hao // 2 + 1):
        if so_hoan_hao % i == 0:
            t += i

    if t == so_hoan_hao:
        ds_so_hoan_hao.append(so_hoan_hao)
print(len(ds_so_hoan_hao))
for so_hoan_hao in ds_so_hoan_hao:
    print(so_hoan_hao)

