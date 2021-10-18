# 어른 상어
from collections import deque


# 방향 인덱스를 0으로 만들기 위해
def minus_1(_str):
    return int(_str) - 1


# 위, 아래, 왼쪽, 오른쪽
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

size, N, K = map(int, input().split())
sharks = [deque() for _ in range(N)]
dir_priority = {}
sea = [[-1] * size for _ in range(size)]
for i in range(size):
    tmp = list(map(int, input().split()))
    for j in range(size):
        if tmp[j]:
            sharks[tmp[j] - 1].append((i, j))
            sea[i][j] = tmp[j] - 1
dead = [False] * N
shark_dir = list(map(minus_1, input().split()))

# 우선순위 딕셔너리 형태로 저장.
for i in range(N):
    dir_priority[i] = {}
    for d in range(4):
        tmp = list(map(minus_1, input().split()))
        dir_priority[i][d] = tmp
result = -1
for second in range(1, K):
    for i in range(N):
        if not dead[i]:
            cur_r, cur_c = sharks[i][-1]
            candidate = 0
            candidate_dir = 0
            for d in dir_priority[i][shark_dir[i]]:
                nr = cur_r + dr[d]
                nc = cur_c + dc[d]

                if 0 <= nr < size and 0 <= nc < size:
                    # 아무냄새가 없는 칸.
                    if sea[nr][nc] == -1:
                        shark_dir[i] = d
                        sharks[i].append((nr, nc))
                        break
                    elif sea[nr][nc] == i and not candidate:
                        candidate = (nr, nc)
                        candidate_dir = d
            else:
                shark_dir[i] = candidate_dir
                sharks[i].append(candidate)
    flag = False
    r, c = sharks[0][-1]
    sea[r][c] = 0
    for i in range(1, N):
        if not dead[i]:
            r, c = sharks[i][-1]
            if sea[r][c] == -1 or sea[r][c] == i:
                flag = True
                sea[r][c] = i
            else:
                sharks[i].pop()
                dead[i] = True

    if not flag:
        result = second
        break

if result == -1:
    for second in range(K, 1001):

        for i in range(N):
            if not dead[i]:
                cur_r, cur_c = sharks[i][-1]
                candidate = 0
                candidate_dir = 0
                for d in dir_priority[i][shark_dir[i]]:
                    nr = cur_r + dr[d]
                    nc = cur_c + dc[d]

                    if 0 <= nr < size and 0 <= nc < size:
                        # 아무냄새가 없는 칸.
                        if sea[nr][nc] == -1:
                            shark_dir[i] = d
                            sharks[i].append((nr, nc))
                            break
                        elif sea[nr][nc] == i and not candidate:
                            candidate = (nr, nc)
                            candidate_dir = d
                else:
                    shark_dir[i] = candidate_dir
                    sharks[i].append(candidate)
        flag = False
        r, c = sharks[0][-1]
        sea[r][c] = 0

        for i in range(N):
            if sharks[i]:
                r, c = sharks[i].popleft()
                if (r, c) not in sharks[i]:
                    sea[r][c] = -1

        for i in range(1, N):
            if not dead[i]:
                r, c = sharks[i][-1]
                if sea[r][c] == -1 or sea[r][c] == i:
                    flag = True
                    sea[r][c] = i
                else:
                    sharks[i].pop()
                    dead[i] = True

        if not flag:
            result = second
            break

print(result)
