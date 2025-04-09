
N = int(input())   
count = [0] * 1001  
 
for i in range(N):
    a = int(input())
    count[a] += 1
 
max_votes = 0
for i in range(1, 1001):
    if count[i] > max_votes:
        max_votes = count[i]
 
result = []
for i in range(1, 1001):
    if count[i] == max_votes:
        result.append(i)

print("\n".join(map(str, result)))
