a = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        if a[i][j] == 1:
            x, y = i + 1, j + 1  
            print(abs(x - 3) + abs(y - 3))
            break