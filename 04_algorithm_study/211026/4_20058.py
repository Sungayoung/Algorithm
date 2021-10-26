# 마법사 상어와 파이어스톰
from copy import deepcopy
import pprint
N, Q = map(int, input().split())

ice = [list(map(int, input().split())) for _ in range(2 ** N)]
size = list(map(int, input().split()))
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

for fire in size:
    fire_size = 1 << fire
    for r in range(0, 1 << N, fire_size):
        for c in range(0, 1 << N, fire_size):
            tmp_ice = [[0] * fire_size for _ in range(fire_size)]

            for i in range(fire_size):
                for j in range(fire_size):
                    tmp_ice[j][fire_size - i - 1] = ice[r + i][c + j]

            for i in range(fire_size):
                for j in range(fire_size):
                    ice[r + i][c + j] = tmp_ice[i][j]
    tmp_ice = deepcopy(ice)
    for r in range(1 << N):
        for c in range(1 << N):
            if ice[r][c] == 0:
                continue
            tmp_cnt = 0
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if 0 <= nr < 1 << N and 0 <= nc < 1 << N and ice[nr][nc]:
                    tmp_cnt += 1
            if tmp_cnt <= 2:
                tmp_ice[r][c] -= 1
    ice = deepcopy(tmp_ice)


visited = [[False] * (1 << N) for _ in range(1 << N)]
max_cnt = 0
result = 0
for r in range(1 << N):
    for c in range(1 << N):
        result += ice[r][c]
        if visited[r][c] or ice[r][c] == 0:
            continue
        visited[r][c] = True
        s = [(r, c)]
        tmp_cnt = 1
        while s:
            cur_r, cur_c = s.pop()
            for d in range(4):
                nr = cur_r + dr[d]
                nc = cur_c + dc[d]

                if 0 <= nr < 1 << N and 0 <= nc < 1 << N and ice[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = True
                    tmp_cnt += 1
                    s.append((nr, nc))
        max_cnt = max(max_cnt, tmp_cnt)

print(result)
print(max_cnt)
