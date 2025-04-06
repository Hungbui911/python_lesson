N = int(input())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

a = [0] + a 

if N == 1:
    print(a[1])
elif N == 2:
    print(a[1] + a[2])
else:
    p2 = a[1]                   
    p1 = a[1] + a[2]             

    for i in range(3, N + 1):
        curr = min(p1 + a[i], p2 + c[i - 3] + a[i])
        p2, p1 = p1, curr

    print(p1)
