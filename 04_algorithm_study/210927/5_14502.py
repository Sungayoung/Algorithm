# 연구소

import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    global min_virus
    q = deque(virus)
    tmp_virus = len(virus)
    visited = [[False] * width for _ in range(height)]
    while q:
        cur = q.popleft()
        for i in range(4):
            nr = cur[0] + dr[i]
            nc = cur[1] + dc[i]
            if 0 <= nr < height and 0 <= nc < width:
                if not visited[nr][nc] and not lab[nr][nc]:
                    visited[nr][nc] = True
                    tmp_virus += 1
                    if tmp_virus > min_virus:
                        return False
                    q.append((nr, nc))
    result = 0
    if tmp_virus < min_virus:
        min_virus = tmp_virus

    for r in range(height):
        for c in range(width):
            if not visited[r][c] and not lab[r][c]:
                result += 1
    return result


# 재귀로 벽 3개 세워줌
def recursion(idx, sel):
    global max_safe

    if sel == 3:
        result = bfs()
        if result:
            if result > max_safe:
                max_safe = result
        return
    for i in range(idx, N):
        if not selected[i] and not lab[i // width][i % width]:
            selected[i] = 1
            lab[i // width][i % width] = 1
            recursion(i, sel + 1)
            selected[i] = 0
            lab[i // width][i % width] = 0


height, width = map(int, input().split())
virus = []
lab = []
selected = [0] * height * width
N = height * width
for i in range(height):
    tmp = list(map(int, input().split()))
    lab.append(tmp)
    for j in range(width):
        if tmp[j] == 2:
            virus.append((i, j))

min_virus = 987654321
max_safe = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

recursion(0, 0)
print(max_safe)
