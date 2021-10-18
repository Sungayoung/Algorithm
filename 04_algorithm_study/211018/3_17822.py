# 원판 돌리기
def is_nearby(_i, _j):
    ans = []

    for _idx in (-1, 1):
        ni = _i + _idx
        nj = _j + _idx

        if 0 <= ni < N:
            ans.append((ni, (head[ni] + _j) % M))
        ans.append((_i, (head[_i] + nj) % M))

    return ans


N, M, T = map(int, input().split())
head = [0] * N
disk = [list(map(int, input().split())) for _ in range(N)]

for _ in range(T):
    disk_idx, d, k = map(int, input().split())

    # 배수인 원판을 회전시킴
    for idx in range(disk_idx, N + 1, disk_idx):
        if d == 0:
            head[idx - 1] = (head[idx - 1] - k) % M
        else:
            head[idx - 1] = (head[idx - 1] + k) % M

    near = []
    # 원판의 수 변형
    for i in range(N):
        for j in range(M):
            # 원판에 수가 남아있으면,
            if disk[i][(head[i] + j) % M]:
                flag = False
                cur = disk[i][(head[i] + j) % M]
                num_idx = is_nearby(i, j)
                for r, c in num_idx:
                    if disk[r][c] == cur:
                        near.append((r, c))
                        flag = True
                if flag:
                    near.append((i, (head[i] + j) % M))

    # 평균을 구해서 원판의 숫자를 변형
    if near:
        for r, c in near:
            disk[r][c] = 0
    else:
        tmp_sum = 0
        tmp_cnt = 0
        for i in range(N):
            for j in range(M):
                if disk[i][j]:
                    tmp_sum += disk[i][j]
                    tmp_cnt += 1
        # ZeroDivisionError 방지
        if tmp_cnt:
            tmp_avg = tmp_sum / tmp_cnt

            for i in range(N):
                for j in range(M):
                    if disk[i][j]:
                        if disk[i][j] > tmp_avg:
                            disk[i][j] -= 1
                        elif disk[i][j] < tmp_avg:
                            disk[i][j] += 1
result = 0
for i in range(N):
    for j in range(M):
        result += disk[i][j]

print(result)
