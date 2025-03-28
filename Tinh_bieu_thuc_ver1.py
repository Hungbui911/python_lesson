#Nhập vào số nguyên dương n>=1 hãy tính kết quả biểu thức sau
# S = 1/3 + 3/5 + 5/7 +...+ (2*n+1)/(2*n+3)
n = int(input())
S = 0
if n>=1:
    for i in range(n+1):
        S += (2*i+1)/(2*i+3)
    print(round(S,2))
else:
    print("NO")

