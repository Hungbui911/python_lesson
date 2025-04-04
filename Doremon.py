#Chú mèo máy Doraemon có n cái bánh cần rán, mỗi cái bánh có hai mặt, mỗi lần rán được một mặt.
#  Doraemon có cái chảo có thể rán được k cái bánh cùng lúc. Mỗi lần rán một mặt bánh tốn 5 phút.
#  Hỏi Doraemon cần bao nhiêu phút để ra hết n cái bánh.

#Chú ý: Thời gian cho bánh vào chảo và vớt bánh ra được coi là không đáng kể.
import math
n, k = map(int, input().split())
S = math.ceil((n * 2) / k) * 5
print(S)
