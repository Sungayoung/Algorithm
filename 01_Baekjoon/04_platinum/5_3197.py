# 백조의 호수
import sys
from collections import deque


def bfs(_start):
    q = deque(_start)
    goal = swan[1]
    _end = set()
    while q:
        cur = q.popleft()

        for d in range(4):
            nr = cur[0] + dr[d]
            nc = cur[1] + dc[d]

            if 0 <= nr < height and 0 <= nc < width and not visited[nr][nc]:
                if (nr, nc) == goal:
                    return False
                elif water[nr][nc] == 'X':
                    _end.add((nr, nc))
                else:
                    visited[nr][nc] = True
                    q.append((nr, nc))
    return _end


input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

height, width = map(int, input().split())
visited = [[False] * width for _ in range(height)]
ice = set()
water = []
swan = []
for r in range(height):
    tmp = list(input().strip())
    for c in range(width):
        if tmp[c] == 'L':
            tmp[c] = '.'
            swan.append((r, c))
        elif tmp[c] == 'X':
            ice.add((r, c))
    water.append(tmp)

day = 1

end = [swan[0]]
visited[swan[0][0]][swan[0][1]] = True
while True:
    # 얼음을 녹인다.
    del_list = []
    for cur_r, cur_c in ice:
        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < height and 0 <= nc < width and water[nr][nc] == '.':
                del_list.append((cur_r, cur_c))
                break

    tmp_ice = set()
    for r, c in del_list:
        water[r][c] = '.'

    for r, c in del_list:
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < height and 0 <= nc < width and water[nr][nc] == 'X':
                tmp_ice.add((nr, nc))

    ice = tmp_ice

    result = bfs(end)
    if not result:
        break
    end = result
    day += 1

print(day)
