#Dãy con tăng liên tục dài nhất
n = int(input())
a = list(map(int, input().split()))

day_dai_nhat = 1
day_hien_tai = 1
vi_tri_bat_dau = 0
vi_tri_hien_tai = 0
for i in range(1,n):
    if a[i] > a[i-1]:
        day_hien_tai += 1
    else:
        if day_hien_tai >= day_dai_nhat:
            day_dai_nhat = day_hien_tai
            vi_tri_bat_dau = vi_tri_hien_tai
        day_hien_tai = 1
        vi_tri_hien_tai = i
if day_hien_tai >= day_dai_nhat:
    day_dai_nhat = day_hien_tai
    vi_tri_bat_dau = vi_tri_hien_tai
day_con = a[vi_tri_bat_dau:vi_tri_bat_dau+day_dai_nhat]
print(day_dai_nhat)
print(" ".join(map(str, day_con)))  
