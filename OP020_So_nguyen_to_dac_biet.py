import math

def so_nguyen_to(n):
    if n < 2:
        return False
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def dao_nguoc_so(n):
    return int(str(n)[::-1])

n = int(input())
count = 0

for _ in range(n):
    num = int(input())
    if num < 0:
        continue  
    if so_nguyen_to(num):
        rev = dao_nguoc_so(num)
        if so_nguyen_to(rev):
            count += 1
 
print(count)
