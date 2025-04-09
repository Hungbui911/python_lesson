import math

def find_x_y(n): 
    if n <= 0:
        return -1, -1

    max_x = int(math.isqrt(n))  
    for x in range(max_x, 0, -1):
        can_x = x * x
        if n % can_x == 0:   
            y = n // can_x   
            return x, y  
    
    return -1, -1  

n = int(input())

x, y = find_x_y(n)

if x == -1:
    print("")
elif y == 1:
    print(x)
elif x == 1:
    print(y)
else:
    print(x, y)
