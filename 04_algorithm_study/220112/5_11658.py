# 구간 합 구하기 3
import math
import sys

input = sys.stdin.readline


def fill_y_tree(st, ed, idx):
    if st == ed:
        fill_x_tree(0, N - 1, 1, idx, st)
        r_idx[st] = idx
        return tree[idx]

    mid = (st + ed) // 2
    left_num = fill_y_tree(st, mid, idx * 2)
    right_num = fill_y_tree(mid + 1, ed, idx * 2 + 1)

    for i in range(size + 1):
        tree[idx][i] = left_num[i] + right_num[i]
    return tree[idx]


def fill_x_tree(st, ed, idx_c, idx_r, row):
    if st == ed:
        tree[idx_r][idx_c] = num_arr[row][st]
        c_idx[st] = idx_c
        return tree[idx_r][idx_c]

    mid = (st + ed) // 2
    left_num = fill_x_tree(st, mid, idx_c * 2, idx_r, row)
    right_num = fill_x_tree(mid + 1, ed, idx_c * 2 + 1, idx_r, row)

    tree[idx_r][idx_c] = left_num + right_num

    return tree[idx_r][idx_c]


def update_tree(_r, _c, _diff):
    while _r > 0:
        tmp_c = _c
        while tmp_c > 0:
            tree[_r][tmp_c] += _diff
            # print(_r, tmp_c, tree[_r][tmp_c])
            tmp_c //= 2
        _r //= 2


def sum_y_tree(st, ed, r1, c1, r2, c2, idx):
    if r1 > ed or r2 < st:
        return 0

    if r1 <= st and ed <= r2:
        # print(st, ed, r1, c1, r2, c2)
        return sum_x_tree(0, N - 1, c1, c2, 1, idx)

    mid = (st + ed) // 2
    left_num = sum_y_tree(st, mid, r1, c1, r2, c2, idx * 2)
    right_num = sum_y_tree(mid + 1, ed, r1, c1, r2, c2, idx * 2 + 1)

    return left_num + right_num


def sum_x_tree(st, ed, left, right, idx_c, idx_r):
    if left > ed or right < st:
        return 0

    if left <= st and ed <= right:
        # print('x', left, right, st, ed, idx_r, idx_c)
        return tree[idx_r][idx_c]

    mid = (st + ed) // 2
    left_num = sum_x_tree(st, mid, left, right, idx_c * 2, idx_r)
    right_num = sum_x_tree(mid + 1, ed, left, right, idx_c * 2 + 1, idx_r)

    return left_num + right_num


N, M = map(int, input().split())
num_arr = [list(map(int, input().split())) for _ in range(N)]

height = math.ceil(math.log2(N))
size = 1 << (height + 1)
tree = [[0] * (size + 1) for _ in range(size + 1)]
r_idx = [0] * N
c_idx = [0] * N
fill_y_tree(0, N - 1, 1)
# print(tree)
for _ in range(M):
    tmp = list(map(int, input().split()))

    if tmp[0] == 0:
        # 바꾸는 연산
        r, c, value = tmp[1:]
        diff = value - num_arr[r - 1][c - 1]
        num_arr[r - 1][c - 1] = value
        update_tree(r_idx[r - 1], c_idx[c - 1], diff)
    else:
        # 합 구하는 연산
        r1, c1, r2, c2 = tmp[1:]
        print(sum_y_tree(0, N - 1, r1 - 1, c1 - 1, r2 - 1, c2 - 1, 1))

# print(r_idx)
# print(c_idx)
