import math

n, m = map(int, input().split())

if n < 0 or m < 0:
    print("NO")
else:
    result = math.comb(n + m, n)  
    print(result)
