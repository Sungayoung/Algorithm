from collections import deque
import sys


def find_passenger_bfs(_r, _c):
    q = deque()
    q.append((_r, _c, 0))
    visited = [[False] * size for _ in range(size)]
    length = [[-1] * size for _ in range(size)]
    length[_r][_c] = 0
    while q:
        _cur_r, _cur_c, _cnt = q.popleft()
        visited[_cur_r][_cur_c] = True
        for _i in range(4):
            _n_r = _cur_r + dr[_i]
            _n_c = _cur_c + dc[_i]

            if 0 <= _n_r < size and 0 <= _n_c < size and not board[_n_r][_n_c] and not visited[_n_r][_n_c]:
                length[_n_r][_n_c] = length[_cur_r][_cur_r] + 1
                q.append((_n_r, _n_c))
    return length


input = sys.stdin.readline

size, M, fuel = map(int, input().split())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
board = [list(map(int, input().split())) for _ in range(size)]

taxi_r, taxi_c = map(int, input().split())
taxi_r -= 1
taxi_c -= 1
passenger = []
goal = []
for _ in range(M):
    tmp = list(map(int, input().split()))
    passenger.append((tmp[0] - 1, tmp[1] - 1))
    goal.append((tmp[2] - 1, tmp[3] - 1))

cnt = 0
while passenger:
    tmp = list(find_passenger_bfs(taxi_r, taxi_c))
    if tmp:
        tmp.sort()
        passenger_idx, lose = passenger.index((tmp[0][1], tmp[0][2])), tmp[0][0]
    else:
        fuel = -1
        break
    fuel -= lose

    if fuel <= 0:
        fuel = -1
        break
    taxi_r, taxi_c = passenger[passenger_idx]
    tmp = find_goal_bfs(taxi_r, taxi_c, goal[passenger_idx])
    if tmp:
        if fuel >= tmp:
            fuel += tmp
        else:
            fuel = -1
            break
    else:
        fuel = -1
        break

    taxi_r, taxi_c = goal[passenger_idx]
    passenger.pop(passenger_idx)
    goal.pop(passenger_idx)

print(fuel)
