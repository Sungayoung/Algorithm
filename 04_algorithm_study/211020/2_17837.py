# 새로운 게임 2
from copy import deepcopy

change_dir = {
    1: 2,
    2: 0,
    3: 1,
    4: 3
}

dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

size, K = map(int, input().split())

# 0: 흰색, 1: 빨간색, 2: 파란색
chess_info = [list(map(int, input().split())) for _ in range(size)]
chessboard = [[[] for _ in range(size)] for _ in range(size)]
idx_list = []
for i in range(K):
    r, c, d = map(int, input().split())
    chessboard[r - 1][c - 1].append([i, change_dir[d]])
    idx_list.append((r - 1, c - 1))

flag = False
result = -1
for turn in range(1, 1001):
    if flag:
        break
    for num in range(K):
        i, j = idx_list[num]
        idx, d = chessboard[i][j][0]

        nr = i + dr[d]
        nc = j + dc[d]

        if 0 <= nr < size and 0 <= nc < size:
            if chess_info[nr][nc] == 0:
                start = 0
                for n in range(len(chessboard[i][j])):
                    if chessboard[i][j][n][0] == num:
                        start = n
                        break
                for n in range(start, len(chessboard[i][j])):
                    tmp_idx, tmp_d = chessboard[i][j][n]
                    idx_list[tmp_idx] = (nr, nc)
                    chessboard[nr][nc].append([tmp_idx, tmp_d])
                chessboard[i][j] = deepcopy(chessboard[i][j][:start])

            elif chess_info[nr][nc] == 1:
                start = 0
                for n in range(len(chessboard[i][j])):
                    if chessboard[i][j][n][0] == num:
                        start = n
                        break
                for n in range(len(chessboard[i][j]) - 1, start - 1, -1):
                    tmp_idx, tmp_d = chessboard[i][j][n]
                    idx_list[tmp_idx] = (nr, nc)
                    chessboard[nr][nc].append([tmp_idx, tmp_d])
                chessboard[i][j] = deepcopy(chessboard[i][j][:start])

            elif chess_info[nr][nc] == 2:
                d = (d + 2) % 4
                nr = i + dr[d]
                nc = j + dc[d]
                start = 0
                for n in range(len(chessboard[i][j])):
                    if chessboard[i][j][n][0] == num:
                        start = n
                        break
                chessboard[i][j][start][1] = d
                if 0 <= nr < size and 0 <= nc < size:
                    if chess_info[nr][nc] == 0:
                        start = 0
                        for n in range(len(chessboard[i][j])):
                            if chessboard[i][j][n][0] == num:
                                start = n
                                break
                        for n in range(start, len(chessboard[i][j])):
                            tmp_idx, tmp_d = chessboard[i][j][n]
                            idx_list[tmp_idx] = (nr, nc)
                            chessboard[nr][nc].append([tmp_idx, tmp_d])
                        chessboard[i][j] = deepcopy(chessboard[i][j][:start])
                    elif chess_info[nr][nc] == 1:
                        start = 0
                        for n in range(len(chessboard[i][j])):
                            if chessboard[i][j][n][0] == num:
                                start = n
                                break
                        for n in range(len(chessboard[i][j]) - 1, start - 1, -1):
                            tmp_idx, tmp_d = chessboard[i][j][n]
                            idx_list[tmp_idx] = (nr, nc)
                            chessboard[nr][nc].append([tmp_idx, tmp_d])
                        chessboard[i][j] = deepcopy(chessboard[i][j][:start])

        else:
            d = (d + 2) % 4
            nr = i + dr[d]
            nc = j + dc[d]
            start = 0
            for n in range(len(chessboard[i][j])):
                if chessboard[i][j][n][0] == num:
                    start = n
                    break
            chessboard[i][j][start][1] = d
            if 0 <= nr < size and 0 <= nc < size:
                if chess_info[nr][nc] == 0:
                    start = 0
                    for n in range(len(chessboard[i][j])):
                        if chessboard[i][j][n][0] == num:
                            start = n
                            break
                    for n in range(start, len(chessboard[i][j])):
                        tmp_idx, tmp_d = chessboard[i][j][n]
                        idx_list[tmp_idx] = (nr, nc)
                        chessboard[nr][nc].append([tmp_idx, tmp_d])
                    chessboard[i][j] = deepcopy(chessboard[i][j][:start])
                elif chess_info[nr][nc] == 1:
                    start = 0
                    for n in range(len(chessboard[i][j])):
                        if chessboard[i][j][n][0] == num:
                            start = n
                            break
                    for n in range(len(chessboard[i][j]) - 1, start - 1, -1):
                        tmp_idx, tmp_d = chessboard[i][j][n]
                        idx_list[tmp_idx] = (nr, nc)
                        chessboard[nr][nc].append([tmp_idx, tmp_d])
                    chessboard[i][j] = deepcopy(chessboard[i][j][:start])
    for i in range(size):
        for j in range(size):
            if len(chessboard[i][j]) >= 4:
                result = turn
                flag = True
                break
        if flag:
            break
    print(chessboard)
    print()

print(result)
