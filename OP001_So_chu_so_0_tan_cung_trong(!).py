#cho số nguyên dương hãy đếm xem trong n! có bao nhiêu chữ số 0 tận cùng
n = int(input())
count = 0
i = 5

while n // i > 0:
    count += n // i
    i *= 5

print(count)
