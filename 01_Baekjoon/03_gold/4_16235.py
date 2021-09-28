# 나무 재태크

import sys

input = sys.stdin.readline

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

size, M, year = map(int, input().split())

plus = [list(map(int, input().split())) for _ in range(size)]
forest = [[5] * size for _ in range(size)]

tree = [[[] for _ in range(size)] for _ in range(size)]

# 시간초과를 막기 위해 접근을 위한 리스트, 값 판별을 위한 세트 두가지를 정의함

for _ in range(M):
    tmp = list(map(int, input().split()))
    tree[tmp[0] - 1][tmp[1] - 1].append(tmp[2])

# 총 지나야 하는 년수만큼 반복
for _ in range(year):
    # 봄 & 여름
    for i in range(size):
        for j in range(size):
            if tree[i][j]:
                dead = 0
                slicing_flag = False
                slicing_idx = 0
                # 한 구역에 여러 나무가 심어져있을 수 있기 때문
                for cur_idx in range(len(tree[i][j]) - 1, -1, -1):
                    # 양분이 부족할 때
                    if forest[i][j] < tree[i][j][cur_idx]:
                        dead += tree[i][j][cur_idx] // 2

                        # 시간 초과를 막기 위해 슬라이싱 연산을 이용, 양분이 처음으로 부족한나무 인덱스를 저장
                        if not slicing_flag:
                            slicing_flag = True
                            slicing_idx = cur_idx + 1
                    else:
                        forest[i][j] -= tree[i][j][cur_idx]
                        if forest[i][j] < 0:
                            forest[i][j] = 0
                        tree[i][j][cur_idx] += 1
                forest[i][j] += dead

                # 양분이 한번이라도 부족했다면 슬라이싱
                if slicing_flag:
                    tree[i][j] = tree[i][j][slicing_idx:len(tree[i][j])]

    # 가을
    for i in range(size):
        for j in range(size):
            if tree[i][j]:
                for idx in range(len(tree[i][j])):
                    if tree[i][j][idx] % 5 == 0:
                        for d in range(8):
                            nr = i + dr[d]
                            nc = j + dc[d]

                            if 0 <= nr < size and 0 <= nc < size:
                                tree[nr][nc].append(1)

    # 겨울
    for i in range(size):
        for j in range(size):
            forest[i][j] += plus[i][j]

result = 0
for i in range(size):
    for j in range(size):
        result += len(tree[i][j])

print(result)

