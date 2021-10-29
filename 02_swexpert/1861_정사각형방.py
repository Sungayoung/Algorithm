# 정사각형 방

def dfs(_r, _c):
    global max_room, max_idx
    s = [(_r, _c)]
    cnt = 0
    while s:
        cur_r, cur_c = s.pop()
        cnt += 1
        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                if room[nr][nc] - room[cur_r][cur_c] == 1:
                    s.append((nr, nc))

    if cnt > max_room:
        max_room = cnt
        max_idx = [_r, _c]

    # 이동할 수 있는 방의 개수가 같은 경우 방번호 비교
    elif cnt == max_room:
        if room[_r][_c] < room[max_idx[0]][max_idx[1]]:
            max_room = cnt
            max_idx = [_r, _c]


dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
for tc in range(int(input())):

    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    max_idx = [0, 0]
    max_room = -1
    for i in range(N):
        for j in range(N):
            dfs(i, j)

    print("#{} {} {}".format(tc+1, room[max_idx[0]][max_idx[1]], max_room))
