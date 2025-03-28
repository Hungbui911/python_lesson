# Đề bài
# YÊU CẦU VIẾT BẰNG CHƯƠNG TRÌNH CON 
# An là một học sinh rất đam mê về Toán học, đặc biệt là các con số.
# An phát hiện ra rằng nếu cho một số nguyên dương n thì luôn tồn tại rất nhiều dãy số dạng 
# 1+2+3+…+k≤n. Tuy nhiên An muốn tìm giá trị k lớn nhất có thể để tạo ra được dãy tổng gồm nhiều số tự nhiên liên tiếp cộng với nhau nhất.
# Ví dụ: Giả sử n = 12 n=12 ta có:
# Dãy 1: 1+2=3<12
# Dãy 2: 1+2+3=6<12
# Dãy 3: 1+2+3+4=10<12
# Dãy 4: 1+2+3+4+5=15>12Vi phạm điều kiện
# Dãy thứ ba là dãy dài nhất với k=4. Các bạn hãy lập trình giúp An tìm giá trị k khi biết đầu vào n.
def tim_k_lon_nhat(n):
    k = 0
    tong = 0
    while tong + (k + 1) <= n:
        k += 1
        tong += k
    return k

n = int(input())
print(tim_k_lon_nhat(n))
