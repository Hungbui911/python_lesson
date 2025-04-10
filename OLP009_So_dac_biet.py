# Đọc đầu vào
N = int(input())  # Số lượng các số
a = list(map(int, input().split()))  # Dãy số a1, a2, ..., aN

# Giới hạn
LIMIT = 10**9

# Tìm các số nguyên tố nhỏ hơn hoặc bằng sqrt(LIMIT)
is_prime = [True] * (int(LIMIT**0.5) + 1)
is_prime[0], is_prime[1] = False, False
primes = []

for i in range(2, int(LIMIT**0.5) + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, int(LIMIT**0.5) + 1, i):
            is_prime[j] = False

# Tạo danh sách các số đặc biệt (số có dạng p * q với p, q là số nguyên tố khác nhau)
special_numbers = set()

for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        p, q = primes[i], primes[j]
        product = p * q
        if product <= LIMIT:
            special_numbers.add(product)

# Chuyển set thành list và sắp xếp
special_numbers = sorted(special_numbers)

# Xử lý từng số trong dãy a để tìm số đặc biệt nhỏ nhất không nhỏ hơn
result = []
for num in a:
    # Duyệt qua danh sách các số đặc biệt
    for sn in special_numbers:
        if sn >= num:
            result.append(sn)
            break

# In kết quả
print(*result)
