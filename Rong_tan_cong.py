# Thầy giáo đang gặp khó khăn với giấc ngủ và muốn giải trí bằng cách tưởng tượng mình đang chiến đấu với lũ rồng kéo đến nhà. 
# Thầy có 4 loại vũ khí để chống lại rồng:
# Dép: Cứ mỗi k con rồng, 1 con bị tấn công.
# Chảo: Cứ mỗi l con rồng, 1 con bị đánh.
# Súng nước: Cứ mỗi m con rồng, 1 con bị bắn.
# Bình xịt hơi cay: Cứ mỗi n con rồng, 1 con bị xịt cay.
# Có tổng cộng d con rồng kéo đến, được đánh số từ 1 đến d. Nhiệm vụ của chúng ta là tính số con rồng bị tấn công ít nhất một lần.
# Lưu ý rằng một con rồng có thể bị tấn công bởi nhiều vũ khí khác nhau, nhưng chúng ta chỉ đếm nó một lần nếu nó bị tấn công.
# Hãy viết chương trình giúp thầy giáo giải quyết vấn đề trên.

k = int(input())
l = int(input())   
m = int(input())
n = int(input())
d = int(input())

rong_bi_tan_cong = set()

for x in [k, l, m, n]:
    for i in range(x, d + 1, x):
        rong_bi_tan_cong.add(i)
print(len(rong_bi_tan_cong))