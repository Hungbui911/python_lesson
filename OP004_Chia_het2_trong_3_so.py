#chia hết 2 trong 3 số 4 6 15
#Cho 2 số a và b. tính xem có bao nhiêu số trong [a,b] chia hết cho 2 trong 3 số 4, 6, 15.
def count_multi(x, a, b):
    return b // x - (a - 1) // x

def count_numbers(a, b):
    c1 = count_multi(12, a, b) - count_multi(60, a, b)
    c2 = count_multi(60, a, b) - count_multi(12, a, b) - count_multi(30, a, b)
    c3 = count_multi(30, a, b) - count_multi(60, a, b)
    
    return c1 + c2 + c3

a, b = map(int, input().split())
print(count_numbers(a, b))