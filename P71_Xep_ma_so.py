n = int(input())

hs = []

for _ in range(n):
    id, diem = map(int, input().split())
    hs.append((id, diem))

hs.sort(key=lambda x: (-x[1], x[0]))

for h in hs:
    print(h[0], h[1])
