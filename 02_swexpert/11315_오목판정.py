def is_boundary(_y, _x):
    if 0 <= _x < size and 0 <= _y < size:
        return True
    else:
        return False

def is_omok():
    for _i in range(size):
        for _j in range(size):
            if omok[_i][_j] == "o":
                for _xy in range(4):
                    tmp_x = _j + dx[_xy]
                    tmp_y = _i + dy[_xy]
                    if is_boundary(tmp_y, tmp_x) and omok[tmp_y][tmp_x] == "o":
                        cnt = 1
                        # 한 방향으로 계속 탐색
                        while is_boundary(tmp_y, tmp_x) and omok[tmp_y][tmp_x] == "o":
                            tmp_x += dx[_xy]
                            tmp_y += dy[_xy]
                            cnt += 1
                        if cnt >= 5:
                            return "YES"
    return "NO"


for tc in range(int(input())):
    size = int(input())
    omok = [list(input()) for _ in range(size)]

    dx = [1, 1, 1, 0]   #우, 우하, 우상, 하
    dy = [0, 1, -1, 1]
    print("#{} {}".format(tc+1, is_omok()))

