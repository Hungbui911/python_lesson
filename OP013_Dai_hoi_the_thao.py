n, k = map(int, input().split())
a = list(map(int, input().split()))
 
count = [0] * k
for x in a:
    count[x % k] += 1
 
result = 0
 
if count[0] > 0:
    result += 1
 
for r in range(1, (k // 2) + 1):
    if r == k - r: 
        result += 1
    else: 
        result += max(count[r], count[k - r])

print(result)
