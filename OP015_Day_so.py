def find_x_and_k(n):
    best_x = -1
    best_k = -1
    k = 2
    while k <= 30:  
        tong = 2**k - 1  
        if n % tong == 0:
            x = n // tong
            if x > 0:  
                best_x = x
                best_k = k
        k += 1
    return best_x, best_k

n = int(input())

x, k = find_x_and_k(n)
print(x, k)
