n = int(input())
 
scores = list(map(int, input().split()))

if n < 2:
    print(-1)
else:
    sorted_scores = sorted(set(scores), reverse=True)
    
    if len(sorted_scores) < 2:
        print(-1)  
    else:
        print(sorted_scores[1])  
