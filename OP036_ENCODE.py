t = int(input()) #sai
i = [int(input()) for _ in range(t)]

kq = []
 
for S in i:
    n = None
    for a in range(1, 27):
        for b in range(1, 27):
            for c in range(1, 27):
                if a + b + c == S:
                    tu = ''.join([chr(96 + x) for x in sorted([a, b, c])])
                    if n is None or tu < n:
                        n = tu
    kq.append(n)
 
for res in kq:
    print(res)
