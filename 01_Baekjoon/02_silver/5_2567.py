# 색종이 - 2

paper = [[0] * 101 for _ in range(101)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(int(input())):
    x, y = map(int, input().split())

    for i in range(y, y + 10):
        for j in range(x, x + 10):
            paper[i][j] = 1

cnt = 0
for i in range(101):
    for j in range(101):
        if paper[i][j] == 1:
            for xy in range(4):
                nx = j + dx[xy]
                ny = i + dy[xy]
                if 0 <= nx < 101 and 0 <= ny < 101 and paper[ny][nx] == 0:
                    cnt += 1
print(cnt)
