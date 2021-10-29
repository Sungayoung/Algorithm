from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(int(input())):
    height, width = map(int, input().split())
    board = [[] for _ in range(height)]
    distance = [[0] * width for _ in range(height)]
    cnt = 0
    q = deque()
    for i in range(height):
        board[i] = input()
        for j in range(width):
            if board[i][j] == 'W':
                q.append((i, j))

    while q:
        cur = q.popleft()
        cnt += 1
        for d in range(4):
            nr = cur[0] + dr[d]
            nc = cur[1] + dc[d]

            if 0 <= nr < height and 0 <= nc < width:
                if not distance[nr][nc] and board[nr][nc] == "L":
                    distance[nr][nc] = distance[cur[0]][cur[1]] + 1
                    q.append((nr, nc))

    result = sum(sum(distance[i]) for i in range(height))
    print("#{} {}".format(tc + 1, result))
