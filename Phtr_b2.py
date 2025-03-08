# Tính phương trình bậc 2
import math

a, b, c = map(int, input().split())

if a == 0:
    if b == 0:
        print("VO SO NGHIEM" if c == 0 else "VO NGHIEM")
    else:
        x = -c / b
        print(f"{x:.2f}" if x != 0 else "0.00")
else:
    denta = b * b - 4 * a * c
    if denta < 0:
        print("VO NGHIEM")
    elif denta == 0:
        x = -b / (2 * a) 
        print(f"{x:.2f}")
    else:
        sqrt_denta = math.sqrt(denta)
        x1 = (-b + sqrt_denta) / (2 * a)
        x2 = (-b - sqrt_denta) / (2 * a)
        print(f"{x1:.2f} {x2:.2f}")