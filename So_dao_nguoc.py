##Viết chương trình tìm số đảo ngược (sai hết do chưa rõ test case của thầy) 
# n = input()
# rev_num = ""

# for num in n:
#     rev_num = num + rev_num
# print(int(rev_num))

# n = int(input())
# if n < 0:  
#     print("NO")
# else:
#     rev_num = ""
#     for num in n:
#         rev_num = num + rev_num  
#     print(int(rev_num[::-1]))  

# n= int(input())
# if n < 0 and n[-1] == '0':
#     print("NO")
# else:
#     num = 0
#     while n > 0:
#         num = num * 10 + n % 10
#         n = n // 10
#     print(num)

# a = input().strip()
# print(a[::-1])

n = int(input()) #Code đúng
if n < 0:  
    print("NO")
else:
    rev_num = ""
    for num in str(n):  
        rev_num = num + rev_num  
    print(rev_num)

# def chuyen(n):
#     n = str(n)
#     n= n[::-1]
#     n = int(n)
#     return n
# n = int(input())
# if n < 1:
#     print("NO")
# else:
#     print(chuyen(n))