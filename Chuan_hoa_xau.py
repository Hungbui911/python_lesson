#Chuẩn hóa lại xâu
xau = input()
xau = xau.split()
xau_chuan_hoa = ''
for i in xau:
    if i != '':
        xau_chuan_hoa += i + ' '
print(xau_chuan_hoa)