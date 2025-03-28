##viết trương trình xác nhận a có phải số nguyên hay không và in ra ngoài màn hình
# a = input()   #Code sai vì thiếu điều kiện
# if a.isdigit():
#     print("YES")
# else:  
#     print("NO")

# a= int(input()) #code sai vì 1 không là số nguyên tố
# kt=True
# for i in range(2,a):
#     if a % i == 0:
#         kt = False
# if kt==True:
#     print("YES")
# else:
#     print("NO")

# a = int(input())  #code sai vì 1 không là số nguyên tố
# if a <= 0:
#     print("NO")
# else:
#     kt = True
#     for i in range(2, int(a ** 0.5) + 1):
#         if a % i == 0:
#             kt = False
#             break
#     if kt == True:
#         print("YES")
#     else:
#         print("NO")

a = int(input()) #code đúng nhưng chưa tối ưu
if a <1:
    print("NO")
else:
    kt = True
    for i in range(2, a):
        if a % i == 0:
            kt = False
    if kt == False or a==1:
        print("NO")
    else:
        print("YES")