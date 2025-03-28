# CHo 2 số nguyên dương a và b. Trong một lần di chuyển bạn có thể tăng a lên 1(tức là thay thế bằng a + 1).
# Nhiệm vụ là tìm ra số lần tối thiểu để a có thể chia hết cho b
# Ví dụ lấy a là 10 b là 4 thì số lần tối thiểu để a chia hết cho b là 2 do 10 + 2 = 12 và 12 chia hết cho 4
# Ví dụ 2: lấy a là 8 và b là 4 thì số lần tối thiểu để a chia hết cho b là 0 do 8 chia hết cho 4
a = int(input())
b = int(input())

r = a % b
if r == 0:
    print(0)
else:
    print(b - r)