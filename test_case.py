# Nhập số N
N = int(input())
 
p = 2

while True: 
    so_nguyen_to = True
    if p > 2 and p % 2 == 0:   
        so_nguyen_to = False
    else:
        i = 2
        while i * i <= p:
            if p % i == 0:
                so_nguyen_to = False
                break
            i += 1

    if so_nguyen_to:
        gan_nguyen_to = p * p
        if gan_nguyen_to >= N:
            print(gan_nguyen_to)
            break
    
    p += 1 if p == 2 else 2

