# 배열에서 이동
from collections import deque
import sys

input = sys.stdin.readline


def bfs(diff):
    for start in range(min_num, max_num - diff + 1, 1):
        end = start + diff
        if not (start <= board[0][0] <= end):
            continue
        visited = [[False] * N for _ in range(N)]
        visited[0][0] = True
        q = deque()
        q.append((0, 0))
        while q:
            cur = q.popleft()
            if cur == (N - 1, N - 1):
                return True
            for d in range(4):
                nr = cur[0] + dr[d]
                nc = cur[1] + dc[d]

                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                    if start <= board[nr][nc] <= end:
                        q.append((nr, nc))
                        visited[nr][nc] = True
    return False


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

min_num = 200
max_num = 0
for i in range(N):
    for j in range(N):
        if board[i][j] < min_num:
            min_num = board[i][j]
        elif board[i][j] > max_num:
            max_num = board[i][j]
right = max_num - min_num
left = 0
pos_diff = []
while left <= right:
    mid = (right + left) // 2
    if bfs(mid):
        pos_diff.append(mid)
        right = mid - 1
    else:
        left = mid + 1
print(min(pos_diff))
