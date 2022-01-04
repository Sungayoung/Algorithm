# 마법사 상어와 복제

from collections import deque


def recursion(sel):
    if sel == 3:
        shark_move.append(selected[:])
        return
    for idx in (2, 0, 6, 4):
        selected[sel] = idx
        recursion(sel + 1)


dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

board = [[[] for _ in range(4)] for _ in range(4)]

shark_move = []
selected = [0] * 3
recursion(0)

M, S = map(int, input().split())
smell = deque()
for _ in range(M):
    x, y, d = map(int, input().split())
    board[x - 1][y - 1].append(d - 1)

shark = list(map(int, input().split()))
shark[0] -= 1
shark[1] -= 1
for _ in range(S):

    new_board = [[[] for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            if board[r][c]:
                for d in board[r][c]:
                    for _ in range(8):
                        nr = r + dr[d]
                        nc = c + dc[d]

                        if 0 <= nr < 4 and 0 <= nc < 4 and [nr, nc] != shark:
                            for s in smell:
                                if [nr, nc] in s:
                                    break
                            else:
                                new_board[nr][nc].append(d)
                                break
                        d = (d - 1) % 8
                    else:
                        new_board[r][c].append(d)

    fish_cnt = -1
    road = []
    for move in shark_move:
        tmp_r = shark[0]
        tmp_c = shark[1]
        tmp_fish_cnt = 0
        tmp_road = []
        for m in move:
            tmp_r += dr[m]
            tmp_c += dc[m]

            if not (0 <= tmp_r < 4 and 0 <= tmp_c < 4):
                break

            if (tmp_r, tmp_c) in tmp_road:
                continue
            tmp_fish_cnt += len(new_board[tmp_r][tmp_c])
            tmp_road.append((tmp_r, tmp_c))
        else:
            if fish_cnt < tmp_fish_cnt:
                fish_cnt = tmp_fish_cnt
                road = move

    tmp_list = []
    for m in road:
        shark[0] += dr[m]
        shark[1] += dc[m]
        if new_board[shark[0]][shark[1]]:
            tmp_list.append(shark[:])
            new_board[shark[0]][shark[1]] = []
    smell.append(tmp_list)
    if len(smell) >= 3:
        smell.popleft()

    for r in range(4):
        for c in range(4):
            board[r][c].extend(new_board[r][c])
    # print(board)
result = 0
for r in range(4):
    for c in range(4):
        result += len(board[r][c])

print(result)
