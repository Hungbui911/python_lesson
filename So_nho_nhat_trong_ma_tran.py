#tìm những số nhỏ nhất trong ma trận nhập vào từ bàn phím
n,m = map(int, input().split())
ma_tran = []

for _ in range(n):
    hang = list(map(int, input().split()))
    ma_tran.append(hang) 

gtnn = float('inf')
vi_tri = []

for i in range(n):
    for j in range(m):
        if ma_tran[i][j] < gtnn:
            gtnn = ma_tran[i][j]
            vi_tri = [(i+1, j+1)]
        elif ma_tran[i][j] == gtnn:
            vi_tri.append((i+1, j+1))
print(gtnn)
for vt in vi_tri:
    print(vt[0], vt[1])
