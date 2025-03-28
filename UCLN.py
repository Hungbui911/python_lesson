#viết tìm ucln của 2 số a và b
def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)
a, b = map(int, input().split())
print(ucln(a, b))
# Viết tìm bcnn của 2 số a và b
def bcnn(a, b):
    return a * b // ucln(a, b)
a, b = map(int, input().split())