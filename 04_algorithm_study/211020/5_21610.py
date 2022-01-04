# 마법사 상어와 비바라기
from copy import deepcopy

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, input().split())

water = [list(map(int, input().split())) for _ in range(N)]
clouds = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]
for _ in range(M):
    d, s = map(int, input().split())
    d -= 1
    visited = [[False] * N for _ in range(N)]
    for cloud in clouds:
        cloud[0] = (cloud[0] + dr[d] * s) % N
        cloud[1] = (cloud[1] + dc[d] * s) % N

        water[cloud[0]][cloud[1]] += 1
        visited[cloud[0]][cloud[1]] = True
    for cloud in clouds:
        cnt = 0
        for _d in range(1, 8, 2):
            nr = cloud[0] + dr[_d]
            nc = cloud[1] + dc[_d]

            if 0 <= nr < N and 0 <= nc < N and water[nr][nc]:
                cnt += 1
        water[cloud[0]][cloud[1]] += cnt
    new_clouds = []
    for r in range(N):
        for c in range(N):
            if water[r][c] >= 2 and not visited[r][c]:
                new_clouds.append([r, c])
                water[r][c] -= 2

    clouds = deepcopy(new_clouds)

result = 0
for r in range(N):
    for c in range(N):
        result += water[r][c]

print(result)
