# 모노미노도미노 2
from collections import deque

block_shape = {
    1: [(0, 0)],
    2: [(0, 0), (0, 1)],
    3: [(0, 0), (1, 0)]
}

blue = []
green = []
score = 0
for _ in range(6):
    blue.append([0] * 4)
    green.append([0] * 4)
for _ in range(int(input())):
    t, r, c = map(int, input().split())

    green_flag = False
    blue_flag = False
    if t == 1:
        tmp_h = 0
        for h in range(6):
            if blue[h][r] == 0:
                tmp_h = h
            else:
                break
        blue[tmp_h][r] = 1
        tmp_h = 0
        for h in range(6):
            if green[h][c] == 0:
                tmp_h = h
            else:
                break
        green[tmp_h][c] = 1
    else:
        i, j = block_shape[t][1]
        tmp_h = 5
        for h in range(6):
            if h + j < 6:
                if blue[h][r] == 1 or blue[h + j][r + i] == 1:
                    break
                else:
                    tmp_h = h

        blue[tmp_h][r] = 1
        blue[tmp_h + j][r + i] = 1

        tmp_h = 5
        for h in range(6):
            if h + i < 6:
                if green[h][c] == 1 or green[h + i][c + j] == 1:
                    break
                else:
                    tmp_h = h
        green[tmp_h][c] = 1
        green[tmp_h + i][c + j] = 1

    idx = 5
    while idx >= 0:
        if sum(green[idx]) == 4:
            green.pop(idx)
            green.insert(0, [0] * 4)
            score += 1
        else:
            idx -= 1
    idx = 5
    while idx >= 0:
        if sum(blue[idx]) == 4:
            blue.pop(idx)
            blue.insert(0, [0] * 4)
            score += 1
        else:
            idx -= 1

    while sum(green[0]) or sum(green[1]):
        green.pop()
        green.insert(0, [0] * 4)

    while sum(blue[0]) or sum(blue[1]):
        blue.pop()
        blue.insert(0, [0] * 4)

print(score)
result = 0

for i in range(6):
    for j in range(4):
        result += green[i][j]
        result += blue[i][j]
print(result)
