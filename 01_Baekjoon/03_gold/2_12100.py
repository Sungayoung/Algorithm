# 2048(Easy)
import copy
import sys
import pprint
input = sys.stdin.readline


def move(_tmp, _dir):
    # 위로
    for _j in range(size):
        if _dir == 'u':
            _num_list = []
            for _idx in range(size):
                if _tmp[_idx][_j] != 0:
                    _num_list.append(_tmp[_idx][_j])
            _mov_idx = 0
            _cur_idx = 0
            while _cur_idx < len(_num_list):
                val = _num_list[_cur_idx]
                if _cur_idx + 1 < len(_num_list) and _num_list[_cur_idx + 1] == val:
                    _tmp[_mov_idx][_j] = val * 2
                    _cur_idx += 2
                else:
                    _tmp[_mov_idx][_j] = val
                    _cur_idx += 1
                _mov_idx += 1
            for _idx in range(_mov_idx, size):
                _tmp[_idx][_j] = 0

        # 아래일때
        elif _dir == 'd':
            _num_list = []
            for _idx in range(size-1, -1, -1):
                if _tmp[_idx][_j] != 0:
                    _num_list.append(_tmp[_idx][_j])
            _mov_idx = size - 1
            _cur_idx = 0
            while _cur_idx < len(_num_list):
                val = _num_list[_cur_idx]
                if _cur_idx + 1 < len(_num_list) and _num_list[_cur_idx + 1] == val:
                    _tmp[_mov_idx][_j] = val * 2
                    _cur_idx += 2
                else:
                    _tmp[_mov_idx][_j] = val
                    _cur_idx += 1
                _mov_idx -= 1
            for _idx in range(_mov_idx, -1, -1):
                _tmp[_idx][_j] = 0

        # 왼쪽일때
        elif _dir == 'l':
            _num_list = []
            for _idx in range(size):
                if _tmp[_j][_idx] != 0:
                    _num_list.append(_tmp[_j][_idx])
            _mov_idx = 0
            _cur_idx = 0
            while _cur_idx < len(_num_list):
                val = _num_list[_cur_idx]
                if _cur_idx + 1 < len(_num_list) and _num_list[_cur_idx + 1] == val:
                    _tmp[_j][_mov_idx] = val * 2
                    _cur_idx += 2
                else:
                    _tmp[_j][_mov_idx] = val
                    _cur_idx += 1
                _mov_idx += 1
            for _idx in range(_mov_idx, size):
                _tmp[_j][_idx] = 0

        # 오른쪽일때
        else:
            _num_list = []
            for _idx in range(size - 1, -1, -1):
                if _tmp[_j][_idx] != 0:
                    _num_list.append(_tmp[_j][_idx])
            _mov_idx = size - 1
            _cur_idx = 0
            while _cur_idx < len(_num_list):
                val = _num_list[_cur_idx]
                if _cur_idx + 1 < len(_num_list) and _num_list[_cur_idx + 1] == val:
                    _tmp[_j][_mov_idx] = val * 2
                    _cur_idx += 2
                else:
                    _tmp[_j][_mov_idx] = val
                    _cur_idx += 1
                _mov_idx -= 1
            for _idx in range(_mov_idx, -1, -1):
                _tmp[_j][_idx] = 0
    # pprint.pprint(_tmp)
    return _tmp


def perm(idx, s_idx):
    if s_idx == R:
        selected.append(sel[:])
        return
    for i in range(0, N):
        sel[s_idx] = dir[i]
        perm(i, s_idx + 1)


# 4개중 5개를 뽑는다.
sel = [0] * 5
dir = ['u', 'd', 'l', 'r']
N = 4
R = 5
selected = []
perm(0, 0)

size = int(input())
game = [list(map(int, input().split())) for _ in range(size)]
max_num = 0
tmp = copy.deepcopy(game)

for select in selected:
    tmp = copy.deepcopy(game)
    for s in select:
        tmp = move(tmp, s)
    tmp_max = max(map(max, tmp))
    if tmp_max == 128:
        print(select)
        pprint.pprint(tmp)
    if tmp_max > max_num:
        max_num = tmp_max
    # print(select)
    # pprint.pprint(tmp)
print(max_num)
