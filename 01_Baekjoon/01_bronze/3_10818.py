# 최소, 최대
import sys
input = sys.stdin.readline
N = int(input())

num_list = list(map(int, input().split()))
min_num = num_list[0]
max_num = num_list[0]
for i in range(N):
    if num_list[i] > max_num:
        max_num = num_list[i]
    if num_list[i] < min_num:
        min_num = num_list[i]

print(min_num, max_num)