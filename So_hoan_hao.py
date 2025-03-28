##Viết trương trình tìm số hoàn hảo nhập vào từ bàn phím
# a = int(input()) #code sai điều kiện
# n = 0 
# for i in range(1,a):
#     if a % i == 0:
#         n += i
# if n == a:
#     print("YES")
# else:    
#     print("NO")

# a = int(input()) #code sai điều kiện
# if a < 1:
#     print("NO")
# else:
#     n = 1  
#     for i in range(2, a // 2 + 1):  
#         if a % i == 0:
#             n += i  
#     if n == a:
#         print("YES")
#     else:    
#         print("NO")

# a = int(input()) #code sai điều kiện
# if a < 1:
#     print("NO")
# else:
#     t = 1
#     i = 2
#     while i <= a // 2:
#         if a % i == 0:
#             t += i
#         i += 1
#     print("YES" if t == a else "NO")

a = int(input()) #code đúng
if a<= 0:
    print("NO")
else:
    n = 0 
    for i in range(1,a):
        if a % i == 0:
            n += i
    if n == a:  
        print("YES")    
    else:
        print("NO")