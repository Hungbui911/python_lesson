#Tìm max trong ma trận nhập vào từ bàn phím
# hang, cot = map(int, input().split())

# ma_tran = []
# for i in range(hang):
#     hang_i = list(map(int, input().split()))
#     ma_tran.append(hang_i)
# for hang_i in ma_tran:
#     gtln = max(hang_i)
#     print(gtln)

m, n = map(int, input().split())

a = []
for i in range(m):
    m_i = list(map(int, input().split()))
    a.append(m_i)
for m_i in a:
    gtln = max(m_i)
    print(gtln)
