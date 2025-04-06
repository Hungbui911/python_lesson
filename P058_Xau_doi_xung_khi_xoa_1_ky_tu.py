s = input().strip()
 
if s == s[::-1]:
    print(s)
else:
    n = len(s)
    found = False
    for i in range(n):
        xau_moi = s[:i] + s[i+1:]  
        if xau_moi == xau_moi[::-1]:
            print(xau_moi)
            found = True
            break
    if not found:
        print(-1)
