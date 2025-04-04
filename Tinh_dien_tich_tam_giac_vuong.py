a,b,c = map(int, input().split())
if a**2 + b**2 == c**2:
    cv = (a+b+c)/2
    dt = (cv*(cv-a)*(cv-b)*(cv-c))**0.5
    print(dt)
else:
    print(-1)

# # Tinh_dien_tich_tam_giac_vuong
import math
a, b, c = map(int, input().split())
if c == math.sqrt(a**2 + b**2): 
    s = (a * b) / 2
    print(round(s,1))
else:
    print(-1)