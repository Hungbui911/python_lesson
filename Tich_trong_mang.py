# Tích lớn nhất của mảng
n = int(input())

arr = list(set(int(input()) for _ in range(n)))  

max1, max2 = float('-inf'), float('-inf')
min1, min2 = float('inf'), float('inf')

for num in arr:
    if num > max1:
        max2, max1 = max1, num
    elif num > max2:
        max2 = num

    if num < min1:
        min2, min1 = min1, num
    elif num < min2:
        min2 = num

max_product = max(max1 * max2, min1 * min2)
print( max_product)