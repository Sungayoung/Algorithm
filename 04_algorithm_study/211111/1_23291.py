# 어항정리
import math

N, K = map(int, input().split())
fishbowl = list(map(int, input().split()))
size = math.ceil(N ** 0.5)
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
square_idx = [[-1] * size for _ in range(size)]
second_idx = [[0] * (N // 4) for _ in range(N // 2)]
r, c = size // 2, size // 2
idx = 1
cnt = 1
d = 0
square_idx[r][c] = 0
while idx < N:
    for _ in range(cnt):
        if idx >= N:
            break
        r += dr[d]
        c += dc[d]
        square_idx[r][c] = idx
        idx += 1

    d = (d + 1) % 4
    for _ in range(cnt):
        if idx >= N:
            break
        r += dr[d]
        c += dc[d]
        square_idx[r][c] = idx
        idx += 1
    d = (d + 1) % 4
    cnt += 1

for i in range(N):
    c = i // (N // 2)
    r = (N // 2) - i % (N // 2) - 1
    second_idx[r][c] = i

cnt = 0
while True:
    cnt += 1
    min_fish = 987654321
    min_fish_list = []
    for i in range(N):
        if fishbowl[i] < min_fish:
            min_fish = fishbowl[i]
            min_fish_list = [i]
        elif fishbowl[i] == min_fish:
            min_fish_list.append(i)

    for idx in min_fish_list:
        fishbowl[idx] += 1

    # 첫번째 물고기 이동
    new_fishbowl = [0] * N
    for r in range(size):
        for c in range(size):
            if square_idx[r][c] == -1:
                continue
            cur_idx = square_idx[r][c]
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[c]
                if 0 <= nr < size and 0 <= nc < size:
                    if square_idx[nr][nc] != -1:
                        n_idx = square_idx[nr][nc]
                        if fishbowl[cur_idx] > fishbowl[n_idx]:
                            new_fishbowl[n_idx] += (fishbowl[cur_idx] - fishbowl[n_idx]) // 5
                            new_fishbowl[cur_idx] -= (fishbowl[cur_idx] - fishbowl[n_idx]) // 5
    print(fishbowl)
    for i in range(N):
        fishbowl[i] += new_fishbowl[i]
    print(fishbowl)
    # 두번째 물고기 이동
    new_fishbowl = [0] * N
    for r in range(N // 2):
        for c in range(N // 4):
            if second_idx[r][c] == -1:
                continue
            cur_idx = second_idx[r][c]
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[c]
                if 0 <= nr < size and 0 <= nc < size:
                    if second_idx[nr][nc] != -1:
                        n_idx = second_idx[nr][nc]
                        if fishbowl[cur_idx] > fishbowl[n_idx]:
                            new_fishbowl[n_idx] += (fishbowl[cur_idx] - fishbowl[n_idx]) // 5
                            new_fishbowl[cur_idx] -= (fishbowl[cur_idx] - fishbowl[n_idx]) // 5
    for i in range(N):
        fishbowl[i] += new_fishbowl[i]

    if max(fishbowl) - min(fishbowl) <= K:
        break

print(cnt)
