# 가스관

from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

pipe = {
    '|': [0, 2],
    '-': [1, 3],
    '+': [0, 1, 2, 3],
    '1': [2, 3],
    '2': [0, 3],
    '3': [0, 1],
    '4': [1, 2]
}

height, width = map(int, input().split())
start = (0, 0)
end = (0, 0)
board = []
for i in range(height):
    tmp = list(input())
    for j in range(width):
        if tmp[j] == 'M':
            tmp[j] = '.'
            start = (i, j)
        elif tmp[j] == 'Z':
            tmp[j] = '.'
            end = (i, j)
    board.append(tmp)

visited = [[False] * width for _ in range(height)]

visited[start[0]][start[1]] = True
visited[end[0]][end[1]] = True
blank = []
q = deque()

for d in range(4):
    nr = start[0] + dr[d]
    nc = start[1] + dc[d]

    if 0 <= nr < height and 0 <= nc < width and board[nr][nc] != '.' and board[nr][nc] != 'Z':
        q.append((nr, nc))
        visited[nr][nc] = True

for d in range(4):
    nr = end[0] + dr[d]
    nc = end[1] + dc[d]

    if 0 <= nr < height and 0 <= nc < width and board[nr][nc] != '.' and board[nr][nc] != 'M':
        q.append((nr, nc))
        visited[nr][nc] = True

# print(q)
pos_dir = set()
while q:
    cur = q.popleft()
    for d in pipe[board[cur[0]][cur[1]]]:
        nr = cur[0] + dr[d]
        nc = cur[1] + dc[d]

        if 0 <= nr < height and 0 <= nc < width and not visited[nr][nc]:
            if board[nr][nc] == '.':
                if not blank:
                    blank = (nr, nc)
                pos_dir.add((d + 2) % 4)
                for dd in range(4):
                    nnr = nr + dr[d]
                    nnc = nc + dc[d]

                    if 0 <= nnr < height and 0 <= nnc < width and not visited[nnr][nnc] and board[nnr][nnc] != '.':
                        q.append((nnr, nnc))
                        visited[nnr][nnc] = True
            else:
                q.append((nr, nc))
                visited[nr][nc] = True

ans = '|'
pos_dir = list(pos_dir)
pos_dir.sort()
for p in pipe:
    if pipe[p] == pos_dir:
        ans = p

print('{} {} {}'.format(blank[0] + 1, blank[1] + 1, ans))
