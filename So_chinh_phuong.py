#Số chính phương
import math

def is_perfect_square(a):
    sqrt_a = math.isqrt(a)  # Tính căn bậc hai và làm tròn xuống số nguyên
    return sqrt_a * sqrt_a == a  # Kiểm tra nếu bình phương lại đúng bằng số ban đầu

# Nhập số nguyên dương a từ bàn phím
a = int(input())

if 0 <= a <= 10**8:
    if is_perfect_square(a):
        print("SQUARE")
    else:
        print("NOT SQUARE")
else:
    print("Gia tri nam ngoai pham vi cho phep")