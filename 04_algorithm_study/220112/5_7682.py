# 틱택토

def is_win(player):
    if board[0][0] == board[0][1] == board[0][2] == player:
        return True
    elif board[1][0] == board[1][1] == board[1][2] == player:
        return True
    elif board[2][0] == board[2][1] == board[2][2] == player:
        return True
    elif board[0][0] == board[1][0] == board[2][0] == player:
        return True
    elif board[0][1] == board[1][1] == board[2][1] == player:
        return True
    elif board[0][2] == board[1][2] == board[2][2] == player:
        return True
    elif board[0][0] == board[1][1] == board[2][2] == player:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


while True:
    line = input()
    if line == 'end':
        break

    board = [['.'] * 3 for _ in range(3)]
    x_count = 0
    o_count = 0
    for i in range(9):
        board[i // 3][i % 3] = line[i]
        if line[i] == 'X':
            x_count += 1
        elif line[i] == 'O':
            o_count += 1
    ans = 'invalid'
    if o_count > x_count or x_count > o_count + 1:
        print(ans)
        continue

    # x가 이긴 경우
    if x_count == o_count + 1 and is_win('X') and not is_win('O'):
        ans = 'valid'
    # o가 이긴 경우
    elif x_count == o_count and is_win('O') and not is_win('X'):
        ans = 'valid'
    # 무승부인 경우
    elif x_count == 5 and o_count == 4 and not is_win('X') and not is_win('O'):
        ans = 'valid'

    print(ans)
