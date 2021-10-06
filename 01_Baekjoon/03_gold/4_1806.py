# 부분합
import sys

input = sys.stdin.readline

N, S = map(int, input().split())
num_list = list(map(int, input().split()))
left = 0
right = 0

while left < N:
    