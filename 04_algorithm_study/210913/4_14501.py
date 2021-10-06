# 퇴사
import sys

input = sys.stdin.readline


def recursion(idx, cur_profit):
    global max_profit
    if idx == N:
        if cur_profit > max_profit:
            max_profit = cur_profit
        return
    if idx > N:
        return
    recursion(idx + 1, cur_profit)
    recursion(idx + counseling[idx][0], cur_profit + counseling[idx][1])


N = int(input())

counseling = [list(map(int, input().split())) for _ in range(N)]
max_profit = 0

recursion(0, 0)

print(max_profit)
