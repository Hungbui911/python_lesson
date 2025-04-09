q = int(input())  
results = []
for _ in range(q):
    n = int(input())   
    total_counter = {}
     
    for _ in range(n):
        s = input().strip()
        for char in s:
            if char in total_counter:
                total_counter[char] += 1
            else:
                total_counter[char] = 1
     
    result = "YES"
    for count in total_counter.values():
        if count % n != 0:
            result = "NO"
            break
    
    results.append(result)  

for result in results:
    print(result)
