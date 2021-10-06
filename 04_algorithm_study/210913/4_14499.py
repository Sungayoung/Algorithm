# 주사위 굴리기
def boundary(_r, _c, _dir):
    if 0 <= _r + dr[_dir - 1] < height and 0 <= _c + dc[_dir - 1] < width:
        return True
    else:
        return False

#   1
# 3 0 2
#   4
#   5


def change_dice_index(_dice, _command):

    # 동, 서 -> 위아래 안바뀜
    if _command == 1:
        dice[0] = _dice[3]
        dice[2] = _dice[0]
        dice[3] = _dice[5]
        dice[5] = _dice[2]
    elif _command == 2:
        dice[0] = _dice[2]
        dice[2] = _dice[5]
        dice[3] = _dice[0]
        dice[5] = _dice[3]

    # 북, 남 -> 좌우 안바뀜
    elif _command == 3:
        dice[0] = _dice[4]
        dice[1] = _dice[0]
        dice[4] = _dice[5]
        dice[5] = _dice[1]
    else:
        dice[0] = _dice[1]
        dice[1] = _dice[5]
        dice[4] = _dice[0]
        dice[5] = _dice[4]



height, width, cur_r, cur_c, k = map(int, input().split())

# 동, 서, 북, 남 순서

board = [list(map(int, input().split())) for _ in range(height)]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

dice = [0] * 6
cur_dice = 0
commands = list(map(int, input().split()))

for command in commands:
    if boundary(cur_r, cur_c, command):
        cur_r += dr[command - 1]
        cur_c += dc[command - 1]
        change_dice_index(dice[:], command)
        if board[cur_r][cur_c] == 0:
            board[cur_r][cur_c] = dice[5]
        else:
            dice[5] = board[cur_r][cur_c]
            board[cur_r][cur_c] = 0

        print(dice[0])