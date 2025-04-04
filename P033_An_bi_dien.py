#An mới học các số nguyên lớn nhưng vẫn nhỏ hơn 1 tỷ. Và An thấy rằng nếu cứ tách các chữ sốcủa số đó ra cộng lại với nhau sẽ được một số mới bé hơn số ban đầu. An rấtthích thú với việc làm đó và cứ mỗi số mới được tạo thành thì An lại tách tiếpcác chữ số ra và cộng chúng lại với nhau. Quá trình này được lặp đi lặp lại chođến khi số được tạo thành chỉ có 1 chữ số.
# Ví dụ: Cho số1234 thì tách được ra thành 1+2+3+4 = 10. Và 10 được tách tiếp thành 1+0 = 1.Cuối cùng An nhận được số 1.
n = int(input())
while n >= 10:
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    n = s
print(n)
