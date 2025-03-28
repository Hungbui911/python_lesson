# Theo quan niệm của người Việt Nam, các số không giảm thường đemlại may mắn và thịnh vượng khi kinh doanh buôn bán. 
# Chính vì vậy các số khônggiảm thường được ưa chuộng bởi rất nhiều người ở Việt Nam. 
# Một số được gọi là không giảm khi các chữ số của chúng đọc lần lượt theo thứ tự từ trái sang phải là không giảm. 
# Ví dụ: Các số không giảm gồm: 6789, 1138, 245, 4, 123456, …
# Các số KHÔNG phải số không giảm gồm: 1354, 654321, 2314, 248753,...
# def is_non_decreasing(n):
#     s = str(n)
#     for i in range(len(s) - 1):
#         if s[i] > s[i + 1]:
#             return False
#     return True
 
# n = int(input().strip())
 
# if is_non_decreasing(n):
#     print("YES")
# else:
#     print("NO")

n = input().strip()  

if all(n[i] <= n[i+1] for i in range(len(n) - 1)):
    print("YES")
else:
    print("NO")


