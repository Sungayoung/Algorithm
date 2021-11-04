# 주사위 굴리기

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

dice_move = [
    [3, 1, 0, 5, 4, 2],
    [1, 5, 2, 3, 0, 4],
    [2, 1, 5, 0, 4, 3],
    [4, 0, 2, 3, 5, 1]
]
height, width, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(height)]
score = [[0] * width for _ in range(height)]
dice = [1, 2, 3, 4, 5, 6]

result = 0

for r in range(height):
    for c in range(width):
        if score[r][c]:
            continue
        visited = [[False] * width for _ in range(height)]
        visited[r][c] = True
        num = board[r][c]
        cnt = 1
        stack = [(r, c)]
        idx = 0
        while idx < len(stack):
            cur_r, cur_c = stack[idx]

            for d in range(4):
                nr = cur_r + dr[d]
                nc = cur_c + dc[d]

                if 0 <= nr < height and 0 <= nc < width and not visited[nr][nc] and board[nr][nc] == num:
                    visited[nr][nc] = True
                    cnt += 1
                    stack.append((nr, nc))
            idx += 1
        for i, j in stack:
            score[r][c] = num * cnt

dice_idx = (0, 0)
d = 0
for _ in range(K):
    nr = dice_idx[0] + dr[d]
    nc = dice_idx[1] + dc[d]

    if not (0 <= nr < height and 0 <= nc < width):
        d = (d + 2) % 4
        nr = dice_idx[0] + dr[d]
        nc = dice_idx[1] + dc[d]
    dice_idx = (nr, nc)
    result += score[nr][nc]
    new_dice = [0] * 6

    for idx, n_idx in enumerate(dice_move[d]):
        new_dice[idx] = dice[n_idx]

    dice = new_dice[:]
    if dice[-1] > board[nr][nc]:
        d = (d + 1) % 4
    elif dice[-1] < board[nr][nc]:
        d = (d - 1) % 4
print(result)