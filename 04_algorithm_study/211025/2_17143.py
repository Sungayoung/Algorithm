# 낚시왕

direction_mapping = {
    1: 0, 2: 2, 3: 1, 4: 3
}
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

height, width, N = map(int, input().split())

board = [[[] for _ in range(width)] for _ in range(height)]

shark = {}

for _ in range(1, N + 1):
    r, c, s, d, z = map(int, input().split())

    board[r - 1][c - 1].append(_)
    shark[_] = [r - 1, c - 1, s, direction_mapping[d], z]
result = 0
for pos in range(width):
    for r in range(height):
        if board[r][pos]:
            result += shark[board[r][pos][0]][4]
            shark[board[r][pos][0]] = 0
            break

    board = [[[] for _ in range(width)] for _ in range(height)]
    for i in shark:
        if shark[i] != 0:
            r, c, s, d, z = shark[i]
            dis = s
            while True:
                if 0 <= r + dis * dr[d] < height and 0 <= c + dis * dc[d] < width:
                    r += dis * dr[d]
                    c += dis * dc[d]
                    break
                else:
                    if dr[d]:
                        dis -= abs(r - (0 if dr[d] == -1 else (height - 1)))
                        r = 0 if dr[d] == -1 else (height - 1)
                    else:
                        dis -= abs(c - (0 if dc[d] == -1 else (width - 1)))
                        c = 0 if dc[d] == -1 else (width - 1)
                    d = (d + 2) % 4
            shark[i] = [r, c, s, d, z]
            board[r][c].append(i)
    for i in range(height):
        for j in range(width):
            if len(board[i][j]) > 1:
                max_size = 0
                max_idx = 0
                for idx in board[i][j]:
                    if shark[idx][4] > max_size:
                        max_idx = idx
                        max_size = shark[idx][4]

                for idx in board[i][j]:
                    if idx != max_idx:
                        shark[idx] = 0

                board[i][j] = [max_idx]

print(result)
