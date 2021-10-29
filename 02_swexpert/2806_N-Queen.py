# N-Queen
import copy


def check_visit(r, c, _visit):

    # 대각선 체크 위함
    length = 0
    for i in range(r, size):
        if 0 <= c - length < size:
            _visit[i][c - length] = True
        if 0 <= c + length < size:
            _visit[i][c + length] = True
        _visit[i][c] = True
        length += 1
    return _visit


def n_queen(sel, visit):
    global answer
    if sel == size:
        answer += 1
        return

    for i in range(size):
        if not visit[sel][i]:
            new_visit = check_visit(sel, i, copy.deepcopy(visit))
            n_queen(sel + 1, copy.deepcopy(new_visit))


for tc in range(int(input())):
    size = int(input())
    answer = 0
    visited = [[False] * size for _ in range(size)]
    n_queen(0, copy.deepcopy(visited))

    print("#{} {}".format(tc + 1, answer))
