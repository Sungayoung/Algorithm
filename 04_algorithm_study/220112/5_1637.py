# 날카로운 눈

import sys
input = sys.stdin.readline

num_cnt = {}
for _ in range(int(input())):
    A, C, B = map(int, input().split())
    tmp_B = B
    if A <= C:
        if num_cnt.get(A):
            num_cnt[A] += 1
        else:
            num_cnt[A] = 1
    while A + B <= C:
        tmp_A = A + B
        if num_cnt.get(tmp_A):
            num_cnt[tmp_A] += 1
        else:
            num_cnt[tmp_A] = 1
        B += tmp_B

for key, value in num_cnt.items():
    if value % 2:
        print(key, value)
        break
