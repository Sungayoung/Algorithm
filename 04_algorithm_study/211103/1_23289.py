# 온풍기 안녕!
from pprint import pprint
from copy import deepcopy

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

height, width, K = map(int, input().split())
temperature = [[0] * width for _ in range(height)]
searches = []
heaters = []
board_info = [[0] * width for _ in range(height)]
walls = {}
for i in range(height):
    tmp = list(map(int, input().split()))
    for j in range(width):
        if 1 <= tmp[j] <= 4:
            heaters.append((i, j, tmp[j] - 1))
        elif tmp[j] == 5:
            searches.append((i, j))

for _ in range(int(input())):
    r, c, t = map(int, input().split())
    board_info[r - 1][c - 1] = 1
    if t == 0:
        board_info[r - 2][c - 1] = 1
        if walls.get((r - 1, c - 1)):
            walls[(r - 1, c - 1)].append((r - 2, c - 1))
        else:
            walls[(r - 1, c - 1)] = [(r - 2, c - 1)]

        if walls.get((r - 2, c - 1)):
            walls[(r - 2, c - 1)].append((r - 1, c - 1))
        else:
            walls[(r - 2, c - 1)] = [(r - 1, c - 1)]
    else:
        board_info[r - 1][c] = 1
        if walls.get((r - 1, c - 1)):
            walls[(r - 1, c - 1)].append((r - 1, c))
        else:
            walls[(r - 1, c - 1)] = [(r - 1, c)]

        if walls.get((r - 1, c)):
            walls[(r - 1, c)].append((r - 1, c - 1))
        else:
            walls[(r - 1, c)] = [(r - 1, c - 1)]


result = 101
for time in range(1, 101):
    for heater in heaters:
        r, c, d = heater
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < height and 0 <= nc < width):
            continue
        temperature[nr][nc] += 5
        heat_list = {(nr, nc)}
        for t in range(4, 0, -1):
            tmp_list = set()
            for i, j in heat_list:
                for p in (-1, 0, 1):
                    ni = i
                    nj = j
                    if d < 2:
                        ni += p
                    else:
                        nj += p
                    if not (0 <= ni < height and 0 <= nj < width):
                        continue
                    # 벽이 있는 곳 통과
                    if board_info[i][j] and (ni, nj) in walls[(i, j)]:
                        continue

                    # 대각선인 경우를 위해 한번 더 점검
                    if board_info[ni][nj] and (ni + dr[d], nj + dc[d]) in walls[(ni, nj)]:
                        continue
                    ni += dr[d]
                    nj += dc[d]

                    if 0 <= ni < height and 0 <= nj < width and (ni, nj) not in tmp_list:
                        temperature[ni][nj] += t
                        tmp_list.add((ni, nj))
            heat_list = tmp_list.copy()
    # pprint(temperature)
    tmp_temperature = [[0] * width for _ in range(height)]
    for r in range(height):
        for c in range(width):
            if temperature[r][c] == 0:
                continue
            tmp_sum = 0
            cur_temp = temperature[r][c]
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if board_info[r][c] and (nr, nc) in walls[(r, c)]:
                    continue

                if 0 <= nr < height and 0 <= nc < width:
                    if temperature[nr][nc] < cur_temp:
                        diff = cur_temp - temperature[nr][nc]
                        tmp_temperature[nr][nc] += diff // 4
                        tmp_sum += diff // 4
            tmp_temperature[r][c] += cur_temp - tmp_sum

    for i in range(1, height-1):
        if tmp_temperature[i][0]:
            tmp_temperature[i][0] -= 1
        if tmp_temperature[i][width - 1]:
            tmp_temperature[i][width - 1] -= 1

    for j in range(width):
        if tmp_temperature[0][j]:
            tmp_temperature[0][j] -= 1
        if tmp_temperature[height - 1][j]:
            tmp_temperature[height - 1][j] -= 1


    for search in searches:
        r, c = search
        if tmp_temperature[r][c] < K:
            break
    else:
        result = time
        break

    temperature = deepcopy(tmp_temperature)

print(result)
