#kiểm tra dấu ngoặc hợp lệ
S = input().strip()

count = 0
for char in S:
    if char == '(':
        count += 1
    elif char == ')':
        count -= 1
    if count < 0:
        print("FALSE")
        break
else:
    if count == 0:
        print("TRUE")
    else:
        print("FALSE")
