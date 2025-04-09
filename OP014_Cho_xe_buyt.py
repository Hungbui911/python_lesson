import math
 
n, d, t0 = map(int, input().split())
s = list(map(int, input().split()))
 
for si in s:
    if si <= t0:
        print(1, end=" ")
    else:
        k = (si - t0 + d - 1) // d  
        print(k + 1, end=" ")
