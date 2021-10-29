# 최소합
from collections import deque
dr = [1, 0]
dc = [0, 1]


for tc in range(int(input())):
    size = int(input())
    board = [list(map(int, input().split())) for _ in range(size)]
    distance = [[987654321] * size for _ in range(size)]
    q = deque()
    q.append((0, 0))
    distance[0][0] = board[0][0]
    while q:
        cur_r, cur_c = q.popleft()
        for i in range(2):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if 0 <= nr < size and 0 <= nc < size:
                # 이동하면서 현재 가지고있는 거리값 + 다음 지점의 값과 다음지점의 거리를 비교
                if board[nr][nc] + distance[cur_r][cur_c] < distance[nr][nc]:
                    distance[nr][nc] = distance[cur_r][cur_c] + board[nr][nc]
                    q.append((nr, nc))
    print("#{} {}".format(tc+1, distance[-1][-1]))
