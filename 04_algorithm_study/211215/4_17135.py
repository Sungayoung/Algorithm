# 캐슬 디펜스
from collections import deque
from copy import deepcopy

dr = [0, -1, 0]
dc = [-1, 0, 1]


def kill(_castle, _archers):
    ans = 0
    enemy_flag = False
    while not enemy_flag:
        enemy = set()
        for archer in _archers:
            if _castle[-1][archer]:
                if (height - 1, archer) not in enemy:
                    ans += 1
                    enemy.add((height - 1, archer))
                continue
            dis = [[987654321] * width for _ in range(height)]
            q = deque()
            q.append((height - 1, archer))
            dis[height - 1][archer] = 1

            while q:
                cur = q.popleft()
                if _castle[cur[0]][cur[1]]:
                    if cur not in enemy:
                        ans += 1
                        enemy.add(cur)
                    break

                for d in range(3):
                    nr = cur[0] + dr[d]
                    nc = cur[1] + dc[d]

                    if 0 <= nr < height and 0 <= nc < width:
                        if dis[nr][nc] > dis[cur[0]][cur[1]] + 1:
                            dis[nr][nc] = dis[cur[0]][cur[1]] + 1
                            if dis[nr][nc] <= distance:
                                q.append((nr, nc))
        for e in enemy:
            _castle[e[0]][e[1]] = 0
        _castle.pop()
        _castle.appendleft([0] * width)

        for i in range(height):
            if sum(_castle[i]):
                break
        else:
            enemy_flag = True

    return ans


def comb(idx, sel):
    global max_enemy

    if sel == 3:
        ans = kill(deepcopy(castle), selected)
        max_enemy = max(max_enemy, ans)
        return

    for i in range(idx, width):
        selected[sel] = i
        comb(i + 1, sel + 1)


height, width, distance = map(int, input().split())

castle = deque(list(map(int, input().split())) for _ in range(height))

selected = [0] * 3
max_enemy = 0

comb(0, 0)
print(max_enemy)

