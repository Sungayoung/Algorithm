import sys

input = sys.stdin.readline

def check_boundary(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    else:
        return False


def blow(r, c, _d):
    result = 0
    temp_sum = 0
    cur_sand = sand[r][c]
    sand[r][c] = 0
    _dr = [[1, -1, 2, -2, 1, -1, 1, -1, 0, 0], [0, 0, 0, 0, -1, -1, 1, 1, 2, 1],
           [-1, 1, -2, 2, -1, 1, -1, 1, 0, 0], [0, 0, 0, 0, 1, 1, -1, -1, -2, -1]]
    _dc = [[0, 0, 0, 0, 1, 1, -1, -1, -2, -1], [-1, 1, -2, 2, -1, 1, -1, 1, 0, 0],
           [0, 0, 0, 0, -1, -1, 1, 1, 2, 1], [-1, 1, -2, 2, -1, 1, -1, 1, 0, 0]]
    _percent = [0.07, 0.07, 0.02, 0.02, 0.01, 0.01, 0.1, 0.1, 0.05]
    for i in range(9):
        tmp_sand = int(cur_sand * _percent[i])
        if check_boundary(r + _dr[_d][i], c + _dc[_d][i]):
            sand[r + _dr[_d][i]][c + _dc[_d][i]] += tmp_sand
        else:
            result += tmp_sand
        temp_sum += tmp_sand

    if check_boundary(r + _dr[_d][9], c + _dc[_d][9]):
        sand[r + _dr[_d][9]][c + _dc[_d][9]] += (cur_sand - temp_sum)
    else:
        result += (cur_sand - temp_sum)
    return result


N = int(input())

sand = [list(map(int, input().split())) for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

sand_sum = 0
cnt = 1
cur_r = N // 2
cur_c = N // 2
d = 0
for _ in range(N - 1):
    for _ in range(cnt):
        cur_r += dr[d]
        cur_c += dc[d]
        sand_sum += blow(cur_r, cur_c, d)
    d = (d + 1) % 4
    for _ in range(cnt):
        cur_r += dr[d]
        cur_c += dc[d]
        sand_sum += blow(cur_r, cur_c, d)
    d = (d + 1) % 4
    cnt += 1
for _ in range(cnt):
    cur_r += dr[d]
    cur_c += dc[d]
    sand_sum += blow(cur_r, cur_c, d)

print(sand_sum)
