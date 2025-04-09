n = int(input())
 
c = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(i, n + 1, i):
        c[j] += 1
 
kq = sum(1 for i in range(1, n + 1) if c[i] == 9)

print(kq)
