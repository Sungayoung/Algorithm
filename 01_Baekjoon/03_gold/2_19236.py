# 청소년 상어

import copy


def find_idx(_num, _fish):
    for _r in range(4):
        for _c in range(4):
            if _fish[_r][_c] == _num:
                return [_r, _c]
    return False


def recursion(_fish, _dir, _shark, _prev):
    global result

    eat = _fish[_shark[0]][_shark[1]]
    _fish[_shark[0]][_shark[1]] = 0

    for i in range(1, 17):
        idx = find_idx(i, _fish)
        if idx:
            cur_dir = _dir[idx[0]][idx[1]]
            for _ in range(9):
                nr = idx[0] + dr[cur_dir]
                nc = idx[1] + dc[cur_dir]
                if 0 <= nr < 4 and 0 <= nc < 4 and [nr, nc] != _shark:
                    _fish[idx[0]][idx[1]], _fish[nr][nc] = _fish[nr][nc], _fish[idx[0]][idx[1]]
                    _dir[idx[0]][idx[1]], _dir[nr][nc] = _dir[nr][nc], cur_dir

                    break
                cur_dir = (cur_dir + 1) % 8

    tmp_shark = _shark[:]
    shark_dir = _dir[_shark[0]][_shark[1]]
    while True:
        tmp_shark[0] += dr[shark_dir]
        tmp_shark[1] += dc[shark_dir]

        if 0 <= tmp_shark[0] < 4 and 0 <= tmp_shark[1] < 4:
            if _fish[tmp_shark[0]][tmp_shark[1]]:
                recursion(copy.deepcopy(_fish), copy.deepcopy(_dir), tmp_shark, _prev + eat)
        else:
            break

    # 최대값 갱신 시
    result = max(result, _prev + eat)


dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

fish = [[0] * 4 for _ in range(4)]
dir = [[0] * 4 for _ in range(4)]

for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(4):
        fish[i][j] = tmp[j * 2]
        dir[i][j] = tmp[j * 2 + 1] - 1

shark = [0, 0]
result = 0
recursion(copy.deepcopy(fish), copy.deepcopy(dir), shark, 0)

print(result)
