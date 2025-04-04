
n = int(input())
num = input().split()
 
for i in range(n):
    for j in range(i + 1, n): 
        if num[i] + num[j] < num[j] + num[i]: 
            num[i], num[j] = num[j], num[i]
 
kq = ''.join(num) 
 
print(kq)
