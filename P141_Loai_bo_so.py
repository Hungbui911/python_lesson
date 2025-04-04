n = int(input().strip()) 
buoc = 0  

while n > 0:
    day_so = 0  
    for d in str(n):  
        if int(d) > day_so:
            day_so = int(d)  
    n -= day_so  
    buoc += 1 

print(buoc)  
