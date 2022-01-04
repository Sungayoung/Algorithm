# 구간 곱 구하기
import math
import sys

input = sys.stdin.readline


def fill_tree(st, ed, idx):
    if st == ed:
        tree[idx] = nums[st]
        nums_idx[st] = idx
        return tree[idx]

    mid = (st + ed) // 2
    left_num = fill_tree(st, mid, idx * 2)
    right_num = fill_tree(mid + 1, ed, idx * 2 + 1)

    tree[idx] = left_num * right_num % 1000000007
    return tree[idx]


# def change_num(idx, num):
#     num_idx = nums_idx[idx]
#     origin_num = nums[idx]
#     tree[num_idx] = num
#     num_idx //= 2
#     while num_idx > 0:
#         tree[num_idx] //= origin_num
#         tree[num_idx] *= num
#         num_idx //= 2

def change_num(st, ed, idx, change_idx):
    if not (st <= change_idx <= ed):
        return

    if st != ed:
        mid = (st + ed) // 2
        change_num(st, mid, idx * 2, change_idx)
        change_num(mid + 1, ed, idx * 2 + 1, change_idx)

        tree[idx] = tree[idx * 2] * tree[idx * 2 + 1] % 1000000007


def print_num(st, ed, left, right, idx):
    if left > ed or right < st:
        return 1

    if left <= st and ed <= right:
        return tree[idx]

    mid = (st + ed) // 2

    left_num = print_num(st, mid, left, right, idx * 2)
    right_num = print_num(mid + 1, ed, left, right, idx * 2 + 1)

    return left_num * right_num


N, M, K = map(int, input().split())

nums = [int(input()) for _ in range(N)]
nums_idx = [0] * N
height = math.ceil(math.log2(N))
size = 1 << (height + 1)
tree = [0] * (size + 1)
fill_tree(0, N - 1, 1)

for _ in range(M + K):
    t, old, new = map(int, input().split())
    if t == 1:
        tree[nums_idx[old - 1]] = new
        change_num(0, N - 1, 1, old - 1)
    else:
        print(print_num(0, N - 1, old - 1, new - 1, 1) % 1000000007)
