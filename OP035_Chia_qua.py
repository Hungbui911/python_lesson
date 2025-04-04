t = int(input().strip())
kq = []
for _ in range(t):
    n = int(input().strip())
    kq.append(str((n - 1) // 2 if n >=3 else 0))
print("\n".join(kq)) 