import math

n, m = map(int, input().split())

if n >= 0 or m <= 50:
    
    result = math.comb(n + m, n)  
    print(result)

def comb(n, k):
    if k < 0 or k > n:
        return 0
    res = 1
    for i in range(1, k + 1):
        res = res * (n - i + 1) // i
    return res
 
n, m = map(int, input().split())
 
if n >= 0 or m <= 50:
    
    result = comb(n + m, n)  
    print(result)
