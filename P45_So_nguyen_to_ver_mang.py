n = int(input())
a = [int(input()) for _ in range(n)]

sl_snt = 0
ds_snt = []

for x in a:
    if x < 2:
        continue
    so_nguyen_to = True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            so_nguyen_to = False
            break
    if so_nguyen_to:
        sl_snt += 1
        ds_snt.append(x)

print(sl_snt)
for so in ds_snt:
    print(so)
