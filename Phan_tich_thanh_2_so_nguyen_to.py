#Viết chương trình nhập vào số nguyên dương x. Hãy viết chương trình phân tích số x thành tổng của 2 số nguyên tố.
x = int(input())
def so_ng_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def tong_so_ng_to(x):
    for i in range(2, x):
        if so_ng_to(i) and so_ng_to(x - i):
            return (i, x - i)
    return None
kq = tong_so_ng_to(x)
if kq:
    for i in kq:
        print(i)
else:
    print("NO")
#Cách 2

def kt_snt(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def phan_tich(n):
    cap_so_TM = None
    khoang_cach_max = 0
    
    for i in range(2, n // 2 + 1):
        j = n - i  
        if kt_snt(i) and kt_snt(j):
            khoang_cach_2_so = abs(j - i)
            if khoang_cach_2_so > khoang_cach_max:  
                cap_so_TM = (i, j)
                khoang_cach_max = khoang_cach_2_so
    
    return cap_so_TM

n = int(input())
result = phan_tich(n)
if result:
    print(result[0])
    print(result[1])
else:
    print(f"NO")