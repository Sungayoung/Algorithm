# 격자판의 숫자 이어붙이기
from collections import deque


def bfs():
    q = deque()
    for r in range(4):
        for c in range(4):
            q.append((r, c, board[r][c]))

    while q:
        cur_r, cur_c, num = q.popleft()

        if len(num) == 7:
            answer.add(num)
            continue

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < 4 and 0 <= nc < 4:
                q.append((nr, nc, num + board[nr][nc]))


dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
for tc in range(int(input())):
    board = [input().split() for _ in range(4)]
    answer = set()
    bfs()
    print("#{} {}".format(tc+1, len(answer)))
