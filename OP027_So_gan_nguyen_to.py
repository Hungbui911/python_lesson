import math
 
n = int(input())
 
gh = int(math.sqrt(n)) + 1
 
so_nguyen_to = [True] * (gh + 1)
so_nguyen_to[0] = so_nguyen_to[1] = False

for i in range(2, int(math.sqrt(gh)) + 1):
    if so_nguyen_to[i]:
        for j in range(i * i, gh + 1, i):
            so_nguyen_to[j] = False
 
for p in range(2, gh + 1):
    if so_nguyen_to[p]:
        gan_nguyen_to = p * p
        if gan_nguyen_to >= n:
            print(gan_nguyen_to)
            break
