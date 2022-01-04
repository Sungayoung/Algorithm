# 파이프 옮기기
import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 1, 1]
dc = [1, 1, 0]

s = [(0, 1, 0)]
ans = 0

while s:
    cur = s.pop()

    blank = 0
    for d in [0, 2]:
        nr = cur[0] + dr[d]
        nc = cur[1] + dc[d]

        if 0 <= nr < N and 0 <= nc < N and not board[nr][nc]:
            blank += 1
            if cur[2] == 1 or cur[2] == d:
                if (nr, nc) == (N-1, N-1):
                    ans += 1
                else:
                    s.append((nr, nc, d))
    if blank == 2:
        nr = cur[0] + dr[1]
        nc = cur[1] + dc[1]

        if 0 <= nr < N and 0 <= nc < N and not board[nr][nc]:
            if (nr, nc) == (N - 1, N - 1):
                ans += 1
            else:
                s.append((nr, nc, 1))

print(ans)

