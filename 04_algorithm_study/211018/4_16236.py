# 아기 상어
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

size = int(input())
shark_idx = 0
shark_size = 2
shark_eat = 0
board = []
for i in range(size):
    tmp = list(map(int, input().split()))
    for j in range(size):
        if tmp[j] == 9:
            tmp[j] = 0
            shark_idx = (i, j)

    board.append(tmp)

time = 0
flag = False
while not flag:

    # 다익스트라
    distance = [[987654321] * size for _ in range(size)]
    visited = [[False] * size for _ in range(size)]
    q = deque()
    q.append(shark_idx)
    distance[shark_idx[0]][shark_idx[1]] = 0
    while q:
        cur_r, cur_c = q.popleft()
        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]
            if 0 <= nr < size and 0 <= nc < size and board[nr][nc] <= shark_size:
                if distance[nr][nc] > distance[cur_r][cur_c] + 1:
                    distance[nr][nc] = distance[cur_r][cur_c] + 1
                    q.append((nr, nc))
    min_dis = 987654321
    min_idx = 0

    # 최소행, 최소열, 최소거리 탐색
    for i in range(size):
        for j in range(size):
            if 0 < board[i][j] < shark_size and distance[i][j] < min_dis:
                min_dis = distance[i][j]
                min_idx = (i, j)

    if min_idx:
        shark_idx = min_idx
        board[shark_idx[0]][shark_idx[1]] = 0
        shark_eat += 1
        if shark_eat == shark_size:
            shark_size += 1
            shark_eat = 0

        time += min_dis
    else:
        flag = True

print(time)
