# 마법사 상어와 파이어볼

import sys
import copy
input = sys.stdin.readline

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

size, M, K = map(int, input().split())

# 3차원 리스트(0: 질량, 1: 속력, 2: 방향)
lattice = [[[] for _ in range(size)] for _ in range(size)]

for _ in range(M):
    fire = list(map(int, input().split()))
    lattice[fire[0]-1][fire[1]-1].append(fire[2:])

for _ in range(K):
    # 1. 모든 파이어볼이 자신의 방향대로 속력만큼 이동
    new_lattice = [[[] for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if lattice[i][j]:
                for fireball in lattice[i][j]:
                    # print(fireball)
                    nr = (i + dr[fireball[2]] * fireball[1]) % size
                    nc = (j + dc[fireball[2]] * fireball[1]) % size
                    new_lattice[nr][nc].append(fireball)

    # 2. 이동이 모두 끝난뒤,
    for i in range(size):
        for j in range(size):
            if len(new_lattice[i][j]) > 1:

                total_weight = 0
                total_speed = 0
                remainder = new_lattice[i][j][0][2] % 2
                flag = False
                for fireball in new_lattice[i][j]:
                    total_weight += fireball[0]
                    total_speed += fireball[1]
                    if fireball[2] % 2 != remainder:
                        flag = True
                total_weight = int(total_weight / 5)
                total_speed = int(total_speed / len(new_lattice[i][j]))
                new_lattice[i][j] = []
                if total_weight > 0:
                    if not flag:
                        for d in range(0, 7, 2):
                            new_lattice[i][j].append([total_weight, total_speed, d])
                    else:
                        for d in range(1, 8, 2):
                            new_lattice[i][j].append([total_weight, total_speed, d])
    lattice = copy.deepcopy(new_lattice)

result = 0
for i in range(size):
    for j in range(size):
        if lattice[i][j]:
            for fireball in lattice[i][j]:
                result += fireball[0]

print(result)
