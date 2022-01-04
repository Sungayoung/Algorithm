# 적록색약

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

N = int(input())

board = [input() for _ in range(N)]

RGB = 0
RG = 0

visited = [[False] * N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if visited[r][c]:
            continue
        RGB += 1
        color = board[r][c]
        s = [(r, c)]
        visited[r][c] = True
        while s:
            cur = s.pop()

            for d in range(4):
                nr = cur[0] + dr[d]
                nc = cur[1] + dc[d]

                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and board[nr][nc] == color:
                    visited[nr][nc] = True
                    s.append((nr, nc))

visited = [[False] * N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if visited[r][c]:
            continue
        RG += 1
        color = [board[r][c]]
        if color[0] == 'R':
            color.append('G')
        elif color[0] == 'G':
            color.append('R')
        s = [(r, c)]
        visited[r][c] = True
        while s:
            cur = s.pop()

            for d in range(4):
                nr = cur[0] + dr[d]
                nc = cur[1] + dc[d]

                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and board[nr][nc] in color:
                    visited[nr][nc] = True
                    s.append((nr, nc))

print(RGB, RG)