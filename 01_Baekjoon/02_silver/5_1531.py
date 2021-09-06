# N: 그림의 개수, M: 불투명도
N, M = map(int, input().split())

image = [[0] * 100 for _ in range(100)]

for idx in range(N):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1-1, x2):
        for y in range(y1-1, y2):
            image[y][x] += 1

result = 0
for i in range(100):
    for j in range(100):
        if image[i][j] > M:
            result += 1

print(result)