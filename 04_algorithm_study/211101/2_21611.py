# 마법사 상어와 블리자드
from pprint import pprint

dir_mapping = {
    1: 3,
    2: 1,
    3: 0,
    4: 2
}
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]


def move_beads():
    _r = N // 2
    _c = N // 2
    _cnt = 1
    _d = 0
    tmp_list = []

    # 입력받는 부분
    for _idx in range(1, N * N):
        _r += dr[_d]
        _c += dc[_d]
        if board[_r][_c]:
            tmp_list.append(board[_r][_c])
        if _idx == _cnt ** 2:
            _d = (_d + 1) % 4
        elif _idx == _cnt ** 2 + _cnt:
            _d = (_d + 1) % 4
            _cnt += 1

    _r = N // 2
    _c = N // 2
    _cnt = 1
    _d = 0
    for _idx in range(1, N * N):
        _r += dr[_d]
        _c += dc[_d]
        board[_r][_c] = tmp_list[_idx - 1] if _idx <= len(tmp_list) else 0
        if _idx == _cnt ** 2:
            _d = (_d + 1) % 4
        elif _idx == _cnt ** 2 + _cnt:
            _d = (_d + 1) % 4
            _cnt += 1


def bomb_beads():
    _r = N // 2
    _c = N // 2
    _cnt = 1
    _d = 0
    cur_num = board[_r][_c - 1]
    cnt_num = 0
    idx_list = []
    tmp_list = []
    flag = False
    for _idx in range(1, N * N):
        _r += dr[_d]
        _c += dc[_d]
        if board[_r][_c] == cur_num:
            tmp_list.append((_r, _c))
            cnt_num += 1
        else:
            if cnt_num >= 4:
                flag = True
                beads[cur_num] += cnt_num
                idx_list.extend(tmp_list)
            tmp_list = [(_r, _c)]
            cur_num = board[_r][_c]
            cnt_num = 1

        if _idx == _cnt ** 2:
            _d = (_d + 1) % 4
        elif _idx == _cnt ** 2 + _cnt:
            _d = (_d + 1) % 4
            _cnt += 1
    for _r, _c in idx_list:
        board[_r][_c] = 0
    return flag


def expand_beads():
    _r = N // 2
    _c = N // 2
    _cnt = 1
    _d = 0
    tmp_list = []
    cur_num = board[_r][_c - 1]
    cnt_num = 0

    # 입력받는 부분
    for _idx in range(1, N * N):
        _r += dr[_d]
        _c += dc[_d]
        if board[_r][_c] == cur_num:
            cnt_num += 1
        else:
            tmp_list.extend((cnt_num, cur_num))
            cur_num = board[_r][_c]
            cnt_num = 1
        if _idx == _cnt ** 2:
            _d = (_d + 1) % 4
        elif _idx == _cnt ** 2 + _cnt:
            _d = (_d + 1) % 4
            _cnt += 1

    _r = N // 2
    _c = N // 2
    _cnt = 1
    _d = 0
    for _idx in range(1, N * N):
        _r += dr[_d]
        _c += dc[_d]
        board[_r][_c] = tmp_list[_idx - 1] if _idx <= len(tmp_list) else 0
        if _idx == _cnt ** 2:
            _d = (_d + 1) % 4
        elif _idx == _cnt ** 2 + _cnt:
            _d = (_d + 1) % 4
            _cnt += 1


N, M = map(int, input().split())
beads = [0] * 4
board = [list(map(int, input().split())) for _ in range(N)]
shark = (N // 2, N // 2)
for _ in range(M):
    d, speed = map(int, input().split())
    d = dir_mapping[d]
    nr = shark[0]
    nc = shark[1]
    for _ in range(speed):
        nr += dr[d]
        nc += dc[d]

        board[nr][nc] = 0
    move_beads()

    while bomb_beads():
        move_beads()
    expand_beads()

result = 0
for idx, cnt in enumerate(beads):
    result += idx * cnt

print(result)
