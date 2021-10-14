# 미세먼지 안녕

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

height, width, seconds = map(int, input().split())
dusts = [list(map(int, input().split())) for _ in range(height)]

cleaner = []
for i in range(height):
    if dusts[i][0] == -1:
        dusts[i][0] = 0
        cleaner.append(i)

for _ in range(seconds):
    new_dust = [[0] * width for _ in range(height)]
    # 모든 방향에서 확산
    for r in range(height):
        for c in range(width):
            tmp = 0
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < height and 0 <= nc < width and not (nr in cleaner and nc == 0):
                    tmp += int(dusts[r][c] / 5)
                    new_dust[nr][nc] += int(dusts[r][c] / 5)

            new_dust[r][c] += dusts[r][c] - tmp

    # 공기청정기 위치 청소
    new_dust[cleaner[0]][0] = 0
    new_dust[cleaner[1]][0] = 0

    # 위쪽 반 시계방향
    cur_idx = [cleaner[0] - 1, 0]
    u = 0
    while cur_idx != [cleaner[0], 0]:
        if not (0 <= cur_idx[0] + dr[u] < cleaner[1] and 0 <= cur_idx[1] + dc[u] < width):
            u = (u + 1) % 4
        next_idx = [cur_idx[0] + dr[u], cur_idx[1] + dc[u]]
        new_dust[cur_idx[0]][cur_idx[1]] = new_dust[next_idx[0]][next_idx[1]]
        cur_idx = next_idx

    # 아래쪽 시계방향
    cur_idx = [cleaner[1] + 1, 0]
    d = 2
    while cur_idx != [cleaner[1], 0]:
        if not (cleaner[1] <= cur_idx[0] + dr[d] < height and 0 <= cur_idx[1] + dc[d] < width):
            d = (d - 1) % 4
        next_idx = [cur_idx[0] + dr[d], cur_idx[1] + dc[d]]
        new_dust[cur_idx[0]][cur_idx[1]] = new_dust[next_idx[0]][next_idx[1]]
        cur_idx = next_idx

    # 공기청정기 위치 청소
    new_dust[cleaner[0]][0] = 0
    new_dust[cleaner[1]][0] = 0
    dusts = new_dust

result = 0
for i in range(height):
    for j in range(width):
        result += dusts[i][j]

print(result)