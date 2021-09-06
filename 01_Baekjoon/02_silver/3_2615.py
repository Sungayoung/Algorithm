board_size = 19
game = []
for _ in range(board_size):
    game.append(list(map(int, input().split())))

# 검은색 : 1, 흰색 : 2

# 대각선을 포함한 총 4가지 방향 (가장 좌상단 점을 기준으로 탐색할거기때문)
dx = [1, 0, 1, 1]
dy = [0, 1, 1, -1]

who = 0
cur_x = 0
cur_y = 0
cnt = 0
flag = False
for i in range(board_size):
    for j in range(board_size):

        if game[i][j]:
            cur_x = j
            cur_y = i
            who = game[i][j]
            for xy in range(4):
                cnt = 1
                temp_x = cur_x + dx[xy]
                temp_y = cur_y + dy[xy]

                if 0 <= temp_x < board_size and 0 <= temp_y < board_size:
                    if game[temp_y][temp_x] == who:

                        temp_y = cur_y
                        temp_x = cur_x
                        # 항상 좌상단을 기준으로 했으므로 반대방향에 같은 값이 있다면 육목
                        if 0 <= temp_x - dy[xy] < board_size and 0 <= temp_y - dy[xy] < board_size and game[temp_y][temp_x] == \
                                game[temp_y - dy[xy]][temp_x - dx[xy]]:
                            continue
                        while 0 <= temp_x + dx[xy] < board_size and 0 <= temp_y + dy[xy] < board_size and game[temp_y][temp_x] == game[temp_y + dy[xy]][temp_x + dx[xy]]:
                            cnt += 1
                            temp_x += dx[xy]
                            temp_y += dy[xy]

                        if cnt == 5:
                            flag = True
                            break
        if flag:
            break

    if flag:
        break
else:
    cnt = 0


if cnt:
    print(who)
    print(cur_y + 1, cur_x + 1)
else:
    print(0)