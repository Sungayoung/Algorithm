# 동전 0
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coin = [int(input()) for _ in range(N)]
cnt = 0
for i in range(N-1, -1, -1):
    if coin[i] <= K:
        cnt += K // coin[i]
        K %= coin[i]

    if K == 0:
        break
print(cnt)