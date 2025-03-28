#Hàm f(n)=1+2−3+4−5+⋯+(−1)^n * n
n = int(input())
print((n + 1) // 2 if n % 2 != 0 else - (n // 2))

#Hàm f(n)=-1+2−3+4−5+⋯+(−1)^n * n
n = int(input())
print(n // 2 if n % 2 == 0 else -(n + 1) // 2)
