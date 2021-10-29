# 보급로
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def dijkstra():
    distance = [[987654321] * size for _ in range(size)]
    q = deque()
    q.append((0, 0))
    distance[0][0] = 0

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < size and 0 <= nc < size:
                if distance[nr][nc] > distance[r][c] + road[nr][nc]:
                    distance[nr][nc] = distance[r][c] + road[nr][nc]
                    q.append((nr, nc))
    return distance[size - 1][size - 1]


for tc in range(int(input())):
    size = int(input())
    road = [list(map(int, input())) for _ in range(size)]
    print("#{} {}".format(tc + 1, dijkstra()))
