#Sắp xếp mảng theo thứ tự chẵn lẻ
n = int(input())
mang = []
for _ in range(n):
    x = int(input())
    mang.append(x)

mang_chan = []
for x in mang:
    if x % 2 == 0:
        mang_chan.append(x)
# mang_chan.sort()
mang_le = []
for x in mang:
    if x % 2 != 0:
        mang_le.append(x)
# mang_le.sort()
print (mang_chan + mang_le)
# for num in mang_chan:
#     print(num)
# for nums in mang_le:
#     print(nums)

# mang_chan = [x for x in mang if x % 2 == 0]
# mang_le = [x for x in mang if x % 2 != 0]