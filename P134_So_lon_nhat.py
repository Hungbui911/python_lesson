#Cho một số nguyên dương X hãy in ra chữ số lớn nhất có trong X.
# Ví dụ: X = 5125263 thì chữ số lớn nhất là 6

x = int(input())
sln = 0
while x > 0:
    so = x % 10
    if so > sln:
        sln = so
    x //= 10
print(sln)