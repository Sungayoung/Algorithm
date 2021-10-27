# 윷놀이

def move(idx, _mal):
    global max_score
    if idx == 10:
        if sum(selected) > max_score:
            max_score = sum(selected)
        return

    for i in range(4):
        if _mal[i] == 0:
            continue
        r, c = _mal[i]
        prev_r, prev_c = r, c
        c += dice[idx]
        if r == 0:
            if c == 5:
                r, c = 1, 0
            elif c == 10:
                r, c = 3, 1
            elif c == 15:
                r, c = 2, 0
        elif r != 4:
            if c > 4:
                r, c = 4, c - 4

        if (r, c) in _mal:
            continue
        if c < len(board[r]) and board[r][c] == 40 and ((0, 20) in _mal or (4, 3) in _mal):
            continue

        if c >= len(board[r]):
            _mal[i] = 0
        else:
            selected[idx] = board[r][c]
            _mal[i] = (r, c)

        move(idx + 1, _mal[:])
        _mal[i] = (prev_r, prev_c)
        selected[idx] = 0


board = [list(range(0, 41, 2)), [10, 13, 16, 19, 25],
         [30, 28, 27, 26, 25], [0, 20, 22, 24, 25], [25, 30, 35, 40]]
dice = list(map(int, input().split()))
selected = [0] * 10
mal = [(0, 0)] * 4
max_score = 0

move(0, mal[:])
print(max_score)
