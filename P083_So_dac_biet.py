N = int(input())  
A = int(input())  
 
str_A = str(A)
tong_so = sum(int(so) for so in str_A)
 
B = A + 1
 
while len(str(B)) == N:
    if sum(map(int, str(B))) == tong_so:
        print(B)
        break
    B += 1
else:
    print(-1)