#Cho n là số nguyên dương. Hãy tìm giá trị nguyên dương k lớn nhất sao cho S(k) < n. 
# Trong đó chuỗi S(k) được định nghĩa như sau : S(k) = 1 + 2 + 3 + … + k.
def tim_k(n):
    k = 0
    tong_k = 0
    while tong_k < n:
        k += 1
        tong_k += k
    return k - 1

n = int(input())

print(tim_k(n))
