N, K = map(int, input().split())
cay = list(map(int, input().split()))

tong_cay = sum(cay)

if tong_cay < K:
    print("CHIU")
else:
    cay_song = sum(cay[:K])
    buoc_di = K - cay_song

    for i in range(K, N):
        cay_song += cay[i] - cay[i - K]
        buoc_di = min(buoc_di, K - cay_song)

    print(buoc_di)
