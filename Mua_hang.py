 
n = int(input())
gia = list(map(int, input().split()))

tong = sum(gia)

if tong % 2 == 0:
    print(tong)
else:
    so_le = [x for x in gia if x % 2 == 1]
    if so_le:
        tong -= min(so_le)
        print(tong)
    else:
        print(0)