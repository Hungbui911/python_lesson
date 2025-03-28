# #Để bài
# An sẽ tham gia một cuộc thi vào ngày cuối cùng của năm 2023. 
# Cuộc thi sẽ bắt đầu lúc 20:00 và kéo dài bốn giờ, đúng cho đến nửa đêm (00:00). 
# Sẽ có 1 bài toán, sắp xếp theo độ khó, tức là bài 1 dễ nhất và bài ” khó nhất. An biết rằng anh ấy sẽ mất 5 x i phút để giải được bài toán thứ i
# Bạn bè của An tổ chức một bữa tiệc đêm giao thừa và An muốn có mặt ở đó lúc nửa đêm (00:00) hoặc sớm hơn. Anh ấy cần ở phút để đi từ nhà đến đó, nơi anh ấy sẽ tham gia cuộc thi trước.
# An có thể giải quyết bao nhiêu bài toán nếu anh ấy muốn tham gia bữa tiệc?
# Dữ liệu vào
# Dòng duy nhất của dữ liệu đầu vào chứa hai số nguyên n và k(1≤n<10,15 k ≤ 240) — số bài toán trong cuộc thi và số phút An cần để đến bữa tiệc từ nhà của mình.
# Dữ liệu ra
# In ra một số nguyên, biểu thị số lượng bài toán tối đa có thể mà An có thể giải được để anh ấy có thể đến bữa tiệc vào lúc nửa đêm hoặc sớm hơn.

# Đọc dữ liệu đầu vào
n= int(input())
k= int(input())
while not (1 <= n <= 10 and 1 <= k <= 240):
    n= int(input())
    k= int(input()) 
thoi_gian_con = 240 - k  
tong_thoi_gian = 0
so_bai_lam = 0

for i in range(1, n + 1):
    tong_thoi_gian += 5 * i
    if tong_thoi_gian > thoi_gian_con:
        break
    so_bai_lam += 1

print(so_bai_lam)
    