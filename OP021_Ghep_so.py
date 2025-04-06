def find_max_min(A, B):
    A = str(A)
    B = str(B)
    
    n, m = len(A), len(B)
    Cmax = []
    Cmin = []
     
    i, j = 0, 0
    while i < n and j < m:
        if A[i] > B[j]:
            Cmax.append(A[i])
            Cmin.append(A[i])
            i += 1
        else:
            Cmax.append(B[j])
            Cmin.append(B[j])
            j += 1
 
    Cmax.extend(A[i:])
    Cmin.extend(B[j:])
     
    Cmax = ''.join(Cmax)
    Cmin = ''.join(Cmin)
    
    return Cmax, Cmin
 
A = int(input())
B = int(input())
 
Cmax, Cmin = find_max_min(A, B)
 
print(Cmax)
print(Cmin)
