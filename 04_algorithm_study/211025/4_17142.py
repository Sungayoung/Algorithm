# 연구소 3
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def bfs():
    q = deque()
    distance = [[987654321] * size for _ in range(size)]
    visited = [[False] * size for _ in range(size)]
    for _i in selected:
        q.append(virus[_i])
        distance[virus[_i][0]][virus[_i][1]] = 0
        visited[virus[_i][0]][virus[_i][1]] = True
    while q:
        cur_r, cur_c = q.popleft()
        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < size and 0 <= nc < size and lab[nr][nc] != 1 and not visited[nr][nc]:
                distance[nr][nc] = distance[cur_r][cur_c] + 1
                visited[nr][nc] = True
                q.append((nr, nc))

    max_value = 0
    for r in range(size):
        for c in range(size):
            if lab[r][c] == 0:
                if distance[r][c] == 987654321:
                    return -1
                else:
                    max_value = max(max_value, distance[r][c])
    return max_value


def comb(idx, sel):
    global result
    if sel == M:
        _tmp = bfs()
        if _tmp != -1:
            result = min(result, _tmp)
        return

    for _i in range(idx, len(virus)):
        selected[sel] = _i
        comb(_i + 1, sel + 1)


size, M = map(int, input().split())
result = 987654321
lab = []
virus = []
for i in range(size):
    tmp = list(map(int, input().split()))
    for j in range(size):
        if tmp[j] == 2:
            virus.append((i, j))
    lab.append(tmp)

selected = [0] * M
comb(0, 0)
print(result if result != 987654321 else -1)
