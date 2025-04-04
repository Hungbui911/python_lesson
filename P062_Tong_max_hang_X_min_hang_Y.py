# Cho ma trận vuông NxN, và 2 số x và y. Hãy tính tổng của sốlớn nhất trên hàng X và số nhỏ nhất trên hàng Y
# (Lưu ý các hàng và các cột được đánh số từ 1)
n, x, y = map(int, input().split())
ma_tran = [list(map(int, input().split())) for _ in range(n)]

max_x = max(ma_tran[x - 1])
min_y = min(ma_tran[y - 1])
tong = max_x + min_y
print(tong)
