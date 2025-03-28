# Một người lính muốn mua chuối ở cửa hàng. Anh ta phải trả k đô la cho quả chuối đầu tiên, 2 x k đô la cho quả chuối thứ hai, v.v. 
# (nói cách khác, anh ta phải trả i x k đô la cho quả chuối thứ 2 ).Anh ta có n đô la. 
# Anh ta phải vay bao nhiêu đô la từ người bạn lính của mình để mua chuối ?
# In ra một số nguyên — số đô la mà người lính phải vay từ bạn mình. Nếu anh ta không phải vay tiền thì ghi 0 .

k = int(input())
n = int(input())
w = int(input())

cost = k * (w * (w + 1)) // 2
borrow = max(0,cost - n)
print(borrow)