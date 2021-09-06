# 수열
import sys

input = sys.stdin.readline
N, K = map(int, input().split())

num_list = list(map(int, input().split()))

max_sum = sum(num_list[0:K])
tmp = max_sum
for i in range(1, N - K + 1):
    tmp = tmp - num_list[i-1] + num_list[i + K - 1]
    if tmp > max_sum:
        max_sum = tmp

print(max_sum)
