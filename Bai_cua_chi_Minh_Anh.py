# Tính phương trình bậc 2
# import math

# a, b, c = map(int, input().split())

# if a == 0:
#     if b == 0:
#         print("VO SO NGHIEM" if c == 0 else "VO NGHIEM")
#     else:
#         x = -c / b
#         print(f"{x:.2f}" if x != 0 else "0.00")
# else:
#     denta = b * b - 4 * a * c
#     if denta < 0:
#         print("VO NGHIEM")
#     elif denta == 0:
#         x = -b / (2 * a) 
#         print(f"{x:.2f}")
#     else:
#         sqrt_denta = math.sqrt(denta)
#         x1 = (-b + sqrt_denta) / (2 * a)
#         x2 = (-b - sqrt_denta) / (2 * a)
#         print(f"{x1:.2f} {x2:.2f}")

# Tích lớn nhất của mảng
# n = int(input())

# arr = list(set(int(input()) for _ in range(n)))  

# max1, max2 = float('-inf'), float('-inf')
# min1, min2 = float('inf'), float('inf')

# for num in arr:
#     if num > max1:
#         max2, max1 = max1, num
#     elif num > max2:
#         max2 = num

#     if num < min1:
#         min2, min1 = min1, num
#     elif num < min2:
#         min2 = num

# max_product = max(max1 * max2, min1 * min2)
# print( max_product)

#Tính năm 
# can = ["CANH", "TAN", "NHAM", "QUY", "GIAP", "AT", "BINH", "DINH", "MAU", "KY"]
# chi = [ "THAN", "DAU", "TUAT", "HOI", "TI", "SUU", "DAN", "MAO", "THIN", "TY", "NGO", "MUI"]

# year = int(input())
# can_index = int(str(year)[-1:])
# chi_index = year % 12
# print(can[can_index] , chi[chi_index])

#Số chính phương
# import math

# def is_perfect_square(a):
#     sqrt_a = math.isqrt(a)  # Tính căn bậc hai và làm tròn xuống số nguyên
#     return sqrt_a * sqrt_a == a  # Kiểm tra nếu bình phương lại đúng bằng số ban đầu

# # Nhập số nguyên dương a từ bàn phím
# a = int(input())

# if 0 <= a <= 10**8:
#     if is_perfect_square(a):
#         print("SQUARE")
#     else:
#         print("NOT SQUARE")
# else:
#     print("Gia tri nam ngoai pham vi cho phep")