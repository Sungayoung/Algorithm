# 구슬 탈출 2
# 왠지 재귀로 풀면 될듯?
# 빨간 공이 빠지면 성공, 파란 공이 빠지면 실패
import sys

input = sys.stdin.readline


def move(_red_r, _red_c, _blue_r, _blue_c, _dir):
    _red_flag = False
    _blue_flag = False
    _red_cnt = 0
    _blue_cnt = 0

    while board[_red_r][_red_c] != '#':
        _red_cnt += 1
        if board[_red_r][_red_c] == 'O':
            _red_flag = True
            break
        _red_r += dr[_dir]
        _red_c += dc[_dir]

    # while문을 돌면서 한번 더 실행되었으므로 복구해줌
    if not _red_flag:
        _red_r -= dr[_dir]
        _red_c -= dc[_dir]

    while board[_blue_r][_blue_c] != '#':
        _blue_cnt += 1
        if board[_blue_r][_blue_c] == 'O':
            _blue_flag = True
            break
        _blue_r += dr[_dir]
        _blue_c += dc[_dir]
    # while문을 돌면서 한번 더 실행되었으므로 복구해줌

    if not _blue_flag:
        _blue_r -= dr[_dir]
        _blue_c -= dc[_dir]

    # 두 구슬이 겹친 경우
    if (_red_r, _red_c) == (_blue_r, _blue_c):
        if _red_cnt < _blue_cnt:
            _blue_r -= dr[_dir]
            _blue_c -= dc[_dir]
        else:
            _red_r -= dr[_dir]
            _red_c -= dc[_dir]

    return _red_r, _red_c, _blue_r, _blue_c, _red_flag, _blue_flag


def game(tc, _r_idx, _b_idx):
    global min_cnt, flag
    if tc == 11:
        return
    _r_flag = False
    _b_flag = False

    for i in range(4):
        _r_r, _r_c, _b_r, _b_c, _r_flag, _b_flag = move(_r_idx[0], _r_idx[1], _b_idx[0], _b_idx[1], i)
        # print(tc, r_idx, b_idx, i, _r_flag, _b_flag)
        if _r_flag and not _b_flag: # 동시에 빠지는 경우 제외
            flag = True
            min_cnt = min(tc, min_cnt)
            continue
        if _b_flag:
            continue
        if _r_idx == (_r_r, _r_c) and _b_idx == (_b_r, _b_c):
            continue

        game(tc + 1, (_r_r, _r_c), (_b_r, _b_c))


height, width = map(int, input().split())

board = [list(input().strip()) for _ in range(height)]

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

r_idx = (0, 0)
b_idx = (0, 0)
min_cnt = 11
flag = False
for i in range(height):
    for j in range(width):
        if board[i][j] == 'B':
            board[i][j] = '.'
            b_idx = (i, j)
        elif board[i][j] == 'R':
            board[i][j] = '.'
            r_idx = (i, j)

game(1, r_idx, b_idx)
if not flag:
    min_cnt = -1

print(min_cnt)

