#chia hết 2 trong 3 số 4 6 15
#Cho 2 số a và b. tính xem có bao nhiêu số trong [a,b] chia hết cho 2 trong 3 số 4, 6, 15.
def count_numbers(a, b):
    def is_valid(x):
        count = 0
        if x % 4 == 0:
            count += 1
        if x % 6 == 0:
            count += 1
        if x % 15 == 0:
            count += 1
        return count == 2

    result = 0
    for x in range(a, b + 1):
        if is_valid(x):
            result += 1
    return result

a,b =map(int, input().split())
print(count_numbers(a, b)) 
