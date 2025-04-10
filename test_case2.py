import math

n = int(input())
s = 0
l = int(n ** 0.5)
 
p = [True] * (l + 1)
p[0] = p[1] = False
ps = []

for i in range(2, l + 1):
    if p[i]:
        ps.append(i)
        for j in range(i * i, l + 1, i):
            p[j] = False
 
for i in range(len(ps)):
    for j in range(i + 1, len(ps)):
        if ps[i] * ps[j] <= l:
            s += 1
        else:
            break
 
for pa in ps:
    if pa ** 8 <= n:
        s += 1
    else:
        break

print(s)
