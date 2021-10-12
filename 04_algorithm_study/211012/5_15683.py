# 감시
from copy import deepcopy


def set_cctv_area(_r, _c, _dir, _num, tmp_safe_area):
    cnt = 0
    for cctv_dir in direction[_num]:
        nr = _r + dr[(_dir + cctv_dir) % 4]
        nc = _c + dc[(_dir + cctv_dir) % 4]
        while 0 <= nr < height and 0 <= nc < width:
            if office[nr][nc] == 6:
                break
            if tmp_safe_area[nr][nc]:
                cnt += 1
            tmp_safe_area[nr][nc] = 0
            nr += dr[(_dir + cctv_dir) % 4]
            nc += dc[(_dir + cctv_dir) % 4]
    return cnt, tmp_safe_area


def perm(idx):
    global max_area
    if idx == len(cctv_list):
        area = 0
        tmp_safe_area = deepcopy(safe_area)
        for sel in range(len(cctv_list)):
            num, r, c = cctv_list[sel]
            tmp_area, tmp_safe_area = set_cctv_area(r, c, selected[sel], num, tmp_safe_area)
            area += tmp_area
        max_area = max(area, max_area)
        return

    for i in range(4):
        selected[idx] = i
        perm(idx + 1)


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

direction = {
    1: [0],
    2: [0, 2],
    3: [0, 3],
    4: [0, 3, 2],
    5: [0, 1, 2, 3]
}
height, width = map(int, input().split())

office = []
cctv_list = []
safe_area = [[1] * width for _ in range(height)]
cctv_5 = []
for i in range(height):
    line = list(map(int, input().split()))
    for j in range(width):
        if line[j]:
            safe_area[i][j] = 0
            if line[j] == 5:
                cctv_5.append((i, j))
            elif line[j] != 6:
                cctv_list.append((line[j], i, j))
    office.append(line)

max_area = 0
selected = [0] * len(cctv_list)
for cctv in cctv_5:
    tmp, safe_area = set_cctv_area(cctv[0], cctv[1], 0, 5, safe_area)
perm(0)

result = 0
for i in range(height):
    for j in range(width):
        result += safe_area[i][j]

print(result - max_area)
