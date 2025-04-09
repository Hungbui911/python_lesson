#Cho dãy số nguyên gồm n phần tử và q truy vấn.
#Mỗi truy vấn có dạng một cặp số nguyên u ,v. Với mỗi truy vấn, bạn cần trả lời câu hỏi số nhỏ nhất trong các số từ vị trí u đến vị trí v trong dãy số.


n, q = map(int, input().split())
arr = list(map(int, input().split()))

day = []
for _ in range(q):
    u, v = map(int, input().split())
    day.append((u, v))

kq = []
for u, v in day: 
    kq.append(min(arr[u-1:v]))

print(" ".join(map(str, kq)))
 



