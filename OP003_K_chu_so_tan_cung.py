#Tìm k chữ số cuối cùng của M^N 
k, m, n = map(int, input().split())

kq = str(m**n).zfill(k)[-k:] 
print(kq)