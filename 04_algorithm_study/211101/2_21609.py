# 상어 중학교
from pprint import pprint

N, M = map(int, input().split())
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

block = [list(map(int, input().split())) for _ in range(N)]

score = 0
block_flag = True
while block_flag:
    block_flag = False
    visited = [[False] * N for _ in range(N)]
    large_group = set()
    large_rainbow = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c] or block[r][c] == -1 or block[r][c] == 0 or block[r][c] == -2:
                continue

            group = {(r, c)}
            s = [(r, c)]
            block_color = block[r][c]
            rainbow = 0
            visited[r][c] = True
            while s:
                cur_r, cur_c = s.pop()
                for d in range(4):
                    nr = cur_r + dr[d]
                    nc = cur_c + dc[d]

                    if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in group:
                        if block[nr][nc] == 0 or block[nr][nc] == block_color:
                            if block[nr][nc] == 0:
                                rainbow += 1
                                group.add((nr, nc))
                                s.append((nr, nc))
                            else:
                                group.add((nr, nc))
                                s.append((nr, nc))
                                visited[nr][nc] = True
            if len(group) >= 2:

                block_flag = True
                if len(large_group) < len(group):
                    large_group = group.copy()
                    large_rainbow = rainbow
                elif len(large_group) == len(group):
                    if rainbow > large_rainbow:
                        large_group = group.copy()
                        large_rainbow = rainbow
                    elif rainbow == large_rainbow:
                        large_group = group.copy()

    score += len(large_group) ** 2

    for r, c in large_group:
        block[r][c] = -2
    for c in range(N):
        r = 0
        tmp = []
        while r < N:
            if block[r][c] == -1:
                idx = r - 1
                for tmp_idx in range(len(tmp)-1, -1, -1):
                    block[idx][c] = tmp[tmp_idx]
                    idx -= 1
                tmp = []
            elif block[r][c] >= 0:
                tmp.append(block[r][c])
                block[r][c] = -2
            r += 1
        if tmp:
            idx = N - 1
            for tmp_idx in range(len(tmp)-1, -1, -1):
                block[idx][c] = tmp[tmp_idx]
                idx -= 1
    for r in range(N):
        c = N-1
        tmp = []
        while c >= 0:
            if block[r][c] == -1:
                idx = c + 1
                for tmp_idx in range(len(tmp) - 1, -1, -1):
                    block[r][idx] = tmp[tmp_idx]
                    idx += 1
                tmp = []
            elif block[r][c] >= 0:
                tmp.append(block[r][c])
                block[r][c] = -2
            c -= 1
        if tmp:
            idx = 0
            for tmp_idx in range(len(tmp)-1, -1, -1):
                block[r][idx] = tmp[tmp_idx]
                idx += 1

    block = list(map(list, zip(*block)))[::-1]

print(score)
