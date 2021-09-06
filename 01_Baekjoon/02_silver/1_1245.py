# 농장 관리
from collections import deque
import sys
import pprint
input = sys.stdin.readline


# bfs를 하며 산을 깎아줌
def bfs(y, x):
    q = deque()
    q.append((y, x))

    while len(q) > 0:
        cur = q.popleft()
        visited[cur[0]][cur[1]] = True
        cur_height = farm[cur[0]][cur[1]]
        farm[cur[0]][cur[1]] = 0
        for i in range(8):
            ny = cur[0] + dy[i]
            nx = cur[1] + dx[i]

            if 0 <= ny < height and 0 <= nx < width and not visited[ny][nx] and farm[ny][nx] <= cur_height:
                q.append((ny, nx))


def farm_height():
    max_idx = (0, 0)
    max_num = 0
    flag = False
    for i in range(height):
        for j in range(width):
            if farm[i][j] > max_num:
                max_idx = (i, j)
                max_num = farm[i][j]
                flag = True

    if flag:
        return max_idx
    else:
        return False


height, width = map(int, input().split())

dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

farm = [list(map(int, input().split())) for _ in range(height)]
visited = [[False] * width for _ in range(height)]
cnt = 0
while True:
    pos = farm_height()
    if not pos:
        break
    else:
        cnt += 1
        bfs(pos[0], pos[1])
print(cnt)