import math

def min_taxi(n):
    return math.ceil(n / 4)
 
n = int(input())
so_taxi = min_taxi(n)
print(so_taxi)
