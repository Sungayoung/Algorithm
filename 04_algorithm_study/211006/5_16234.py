# 인구이동
from collections import deque
import sys

input = sys.stdin.readline


def bfs(_r, _c):
    global visited

    q = deque()
    q.append((_r, _c))
    result = {(_r, _c)}
    visited[_r][_c] = True
    while q:
        cur_r, cur_c = q.popleft()

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if L <= abs(people[cur_r][cur_c] - people[nr][nc]) <= R:
                    visited[nr][nc] = True
                    result.add((nr, nc))
                    q.append((nr, nc))

    result = list(result)
    if len(result) == 1:
        return False
    return result


def move_people(border_list):
    global people

    for border in border_list:
        population = 0
        for country in border:
            population += people[country[0]][country[1]]

        change_population = population // len(border)
        for country in border:
            people[country[0]][country[1]] = change_population


N, L, R = map(int, input().split())

people = [list(map(int, input().split())) for _ in range(N)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
flag = False
day = 0
while not flag:
    visited = [[False] * N for _ in range(N)]
    borders = []
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                tmp = bfs(r, c)
                if tmp:
                    borders.append(tmp)
    if borders:
        move_people(borders)
        day += 1
    else:
        flag = True

print(day)
