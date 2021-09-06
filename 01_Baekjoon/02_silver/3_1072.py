# 게임
import math
total_game, cur_win_game = map(int, input().split())

percent = cur_win_game * 100 // total_game
result = 0
if percent >= 99:
    result = -1
else:
    # 앞으로 할 게임횟수를 x로 두고 방정식
    result = math.ceil(((percent + 1) * total_game - 100 * cur_win_game)/(100 - (percent + 1)))

print(result)
