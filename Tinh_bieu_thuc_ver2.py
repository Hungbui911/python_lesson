#Nhập vào số nguyên dương n>=1 hãy tính kết quả biểu thức sau
# S = 1/1 + 1/3 + 1/5 +...+ 1/(2*n+1)
# n = int(input()) #why sai ?
# S = 0
# for i in range(n+1):
#     mau_so = 2*i+1
#     S += 1/mau_so
# print(round(S,2))

n = int(input()) 
if n > 1:
    S = sum(1 / (2 * i + 1) for i in range(n+1))
    print(round(S, 2))
