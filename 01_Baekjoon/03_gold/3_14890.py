# 경사로

size, L = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(size)]
result = 0
for i in range(size):
    # 가로방향
    flag = True
    prev_value = board[i][0]
    idx = 0
    visited = [False] * size
    while idx < size and flag:
        if board[i][idx] == prev_value:
            idx += 1
        elif board[i][idx] - prev_value == -1:
            if visited[idx]:
                flag = False
                break
            cnt = 1
            n_value = board[i][idx]
            visited[idx] = True
            while cnt < L:
                if idx + cnt >= size or visited[idx + cnt] or board[i][idx + cnt] != n_value:
                    flag = False
                    break
                visited[idx + cnt] = True
                cnt += 1
            else:
                prev_value = n_value
                idx += L
        elif board[i][idx] - prev_value == 1:
            cnt = 1
            while cnt < L + 1:
                if idx - cnt < 0 or visited[idx - cnt] or board[i][idx - cnt] != prev_value:
                    flag = False
                    break
                visited[idx - cnt] = True
                cnt += 1
            else:
                prev_value = board[i][idx]
                idx += 1
        else:
            flag = False
    if flag:
        result += 1

    # 세로방향
    flag = True
    prev_value = board[0][i]
    idx = 0
    visited = [False] * size
    while idx < size and flag:
        if board[idx][i] == prev_value:
            idx += 1
        elif board[idx][i] - prev_value == -1:
            if visited[idx]:
                flag = False
                break
            cnt = 1
            n_value = board[idx][i]
            visited[idx] = True
            while cnt < L:
                if idx + cnt >= size or visited[idx + cnt] or board[idx + cnt][i] != n_value:
                    flag = False
                    break
                visited[idx + cnt] = True
                cnt += 1
            else:
                prev_value = n_value
                idx += L
        elif board[idx][i] - prev_value == 1:
            cnt = 1
            while cnt < L + 1:
                if idx - cnt < 0 or visited[idx - cnt] or board[idx - cnt][i] != prev_value:
                    flag = False
                    break
                visited[idx - cnt] = True
                cnt += 1
            else:
                prev_value = board[idx][i]
                idx += 1
        else:
            flag = False
    if flag:
        result += 1

print(result)
