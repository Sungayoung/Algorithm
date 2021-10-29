#   문자	의미
#   .	평지(전차가 들어갈 수 있다.)
#   *	벽돌로 만들어진 벽
#   #	강철로 만들어진 벽
#   -	물(전차는 들어갈 수 없다.)
#   ^	위쪽을 바라보는 전차(아래는 평지이다.)
#   v	아래쪽을 바라보는 전차(아래는 평지이다.)
#   <	왼쪽을 바라보는 전차(아래는 평지이다.)
#   >	오른쪽을 바라보는 전차(아래는 평지이다.)

def key_input(_word, _cur):
    if _word == "U":
        return (-1, 0), "^"
    elif _word == "D":
        return (1, 0), "v"
    elif _word == "L":
        return (0, -1), "<"
    elif _word == "R":
        return (0, 1), ">"
    elif _word == "S":
        return direction(_cur), _cur


def direction(_word):
    if _word == "^":
        return -1, 0
    elif _word == "v":
        return 1, 0
    elif _word == ">":
        return 0, 1
    elif _word == "<":
        return 0, -1


def find_idx():
    car_list = ["^", "v", "<", ">"]
    for _i in range(height):
        for _j in range(width):
            if game_map[_i][_j] in car_list:
                return (_i, _j), game_map[_i][_j]


T = int(input())

for tc in range(T):
    height, width = map(int, input().split())
    game_map = [list(input().strip()) for _ in range(height)]

    cur_pos, cur_state = find_idx()

    key_list = list(input().strip())
    for key in key_list:
        i
