n = int(input()) 
arr = []
for i in range(n):
    so = int(input())
    arr.append(so)
tong_chan = sum(x for x in arr if x % 2 == 0)
arr.sort()
print(tong_chan)
for so in arr:
    print(so)
