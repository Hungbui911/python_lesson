#viết chương trình tính diện tích tam giác nếu thỏa mãn điều kiện là tam giác vuông

a, b, c = map(int, input().split())

canh = [a, b, c]
canh.sort()
 
if canh[0] + canh[1] > canh[2] and canh[0]+canh[2]>canh[1] and canh[1]+canh[2]>canh[0]:
    if canh[0]**2 + canh[1]**2 == canh[2]**2:
        S = (canh[0] * canh[1]) / 2
        print(round(S, 1))
    else:
        print(-1)
else:
    print(-1)