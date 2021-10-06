# 달이 차오른다, 가자.
import sys
from collections import deque

input = sys.stdin.readline


def bfs(_r, _c):
    q = deque()
    key = []
    q.append(((_r, _c), 0))
    visited = [[False] * width for _ in range(height)]
    while q:
        tmp = q.popleft()
        cur = tmp[0]
        cnt = tmp[1]
        print(tmp, key)
        if maze[cur[0]][cur[1]] == "1":
            return cnt
        elif 97 <= ord(maze[cur[0]][cur[1]]) <= 102:
            key.append(maze[cur[0]][cur[1]])
            # 방문 리셋
            visited = [[False] * width for _ in range(height)]
            maze[cur[0]][cur[1]] = "."
        visited[cur[0]][cur[1]] = True
        for i in range(4):
            nr = cur[0] + dr[i]
            nc = cur[1] + dc[i]

            if 0 <= nr < height and 0 <= nc < width and not visited[nr][nc]:
                # 벽인 경우
                if maze[nr][nc].isalpha():
                    # 문
                    if 65 <= ord(maze[nr][nc]) <= 70:
                        if chr(ord(maze[nr][nc]) + 32) in key:
                            q.append(((nr, nc), cnt + 1))
                    # 열쇠
                    elif 97 <= ord(maze[nr][nc]) <= 102:
                        q.append(((nr, nc), cnt + 1))
                else:
                    if maze[nr][nc] == "." or maze[nr][nc] == "1":
                        q.append(((nr, nc), cnt + 1))

    return -1


# A - F : 65 - 70
# a - f : 97 - 102
height, width = map(int, input().split())
maze = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
start = (0, 0)
for i in range(height):
    tmp = list(input())
    maze.append(tmp)
    for j in range(width):
        if tmp[j] == '0':
            start = (i, j)
            maze[i][j] = '.'

print(bfs(start[0], start[1]))
