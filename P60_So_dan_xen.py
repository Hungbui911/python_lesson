n = int(input())
arr = list(map(int, input().split()))
count = 0

for num in arr:
    num_str = str(num)
    so_dan_xen = True
    
    if len(num_str) > 1:
        for i in range(len(num_str) - 1):
            if (int(num_str[i])%2 == int(num_str[i+1])%2):
                so_dan_xen = False
                break
    if so_dan_xen:
        count += 1
print(count)
