# 최소비용
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs():
    distance = [[987654321] * size for _ in range(size)]
    distance[0][0] = 0
    q = deque()
    q.append((0, 0))
    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < size and 0 <= nc < size:
                cost = 1 if board[r][c] >= board[nr][nc] else board[nr][nc] - board[r][c] + 1
                if distance[nr][nc] > distance[r][c] + cost:
                    distance[nr][nc] = distance[r][c] + cost
                    q.append((nr, nc))

    return distance[-1][-1]


for tc in range(int(input())):
    size = int(input())
    board = [list(map(int, input().split())) for _ in range(size)]
    print("#{} {}".format(tc + 1, bfs()))
