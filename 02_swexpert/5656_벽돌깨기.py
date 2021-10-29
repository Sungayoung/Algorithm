# 벽돌깨기
from copy import deepcopy
from collections import deque


def perm(idx):
    if idx == N:
        answer.append(selected[:])
        return

    for i in range(width):
        selected[idx] = i
        perm(idx + 1)


def remain_block():
    """

    Returns: 남아있는 벽돌의 개수를 리턴함

    """
    result = 0
    for _i in range(width):
        for _j in range(height):
            if tmp_board[_i][_j]:
                result += 1
    return result


def reset_block():
    """

    Returns: 중간중간 제거된 벽돌을 재 정렬함

    """
    new_board = [[] for _ in range(width)]
    for _i in range(width):
        idx = 0
        for _j in range(height):
            if tmp_board[_i][_j]:
                new_board[_i].append(tmp_board[_i][_j])
                idx += 1
        while idx < height:
            new_board[_i].append(0)
            idx += 1
    return new_board


def bomb_attack(_pos):
    """

    Args:
        _pos: 구슬을 놓을 위치를 정함

    Returns: 정해진 위치의 벽돌을 제거함

    """
    r = _pos
    c = height - 1
    while c >= 0 and not tmp_board[r][c]:
        c -= 1

    if c < 0:
        return

    q = deque()
    q.append((r, c, tmp_board[r][c]))
    tmp_board[r][c] = 0

    while q:
        cur_r, cur_c, length = q.popleft()
        for l in range(1, length):
            for d in range(4):
                nr = cur_r + dr[d] * l
                nc = cur_c + dc[d] * l

                if 0 <= nr < width and 0 <= nc < height:
                    if tmp_board[nr][nc]:
                        q.append((nr, nc, tmp_board[nr][nc]))
                        tmp_board[nr][nc] = 0


dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

for tc in range(int(input())):
    N, width, height = map(int, input().split())

    tmp = [list(map(int, input().split())) for _ in range(height)]
    board = [[] for _ in range(width)]

    # 계산을 쉽게 하기 위해서 벽돌을 돌림
    for i in range(height - 1, -1, -1):
        for j in range(width):
            board[j].append(tmp[i][j])

    selected = [0] * N
    answer = []
    perm(0)

    min_block = 987654321
    # 구슬을 놓을 수 있는 모든 케이스
    for case in answer:
        tmp_board = deepcopy(board)
        for pos in case:
            bomb_attack(pos)
            tmp_board = reset_block()

        min_block = min(min_block, remain_block())
        # 모든 벽돌이 제거된 경우 반복문을 끝냄
        if min_block == 0:
            break
    print("#{} {}".format(tc + 1, min_block))
