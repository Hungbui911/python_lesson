# Tính biểu thức nhiều căn
# S = √(x^n + √(x^(n-1)+...+√x^1))
# import math

# x, n = float(input()), int(input())
 
# if n>=1:
#     S = math.sqrt(x) 
#     for i in range(2, n+1):
#         S = math.sqrt(x**i + S)

#     print(round(S, 2))
# else:
#     print("NO")


# import math

# x, n = float(input()), int(input())

# if 1 <= n <= 10 and 1 <= x <= 10**2:
#     S = math.sqrt(x)
#     for i in range(2, n + 1):
#         term = x**i + S
#         if term < 0:  
#             break
#         S = math.sqrt(term)
#     else:
#         print(round(S, 2))  
# else:
#     print("NO")

x, n = map(float, input().split()) 
n = int(n)

S = x ** 0.5 
for i in range(2,n+1):
    S = (x ** i + S) ** 0.5 

print(round(S, 2))

