# 로봇청소기
import sys

input = sys.stdin.readline

height, width = map(int, input().split())

# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

r, c, d = map(int, input().split())
place = [list(map(int, input().split())) for _ in range(height)]
clean = [[0] * width for _ in range(height)]
flag = False
while not flag:

    # 현재 위치를 청소
    clean[r][c] = 1
    cnt = 0

    while cnt <= 4:
        if cnt < 4:
            nd = (d - 1) % 4
            nr = r + dr[nd]
            nc = c + dc[nd]

            if 0 <= nr < height and 0 <= nc < width:

                # a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
                if not place[nr][nc] and not clean[nr][nc]:
                    d = nd
                    r = nr
                    c = nc
                    break

                # b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
                elif place[nr][nc] or clean[nr][nc]:
                    d = nd
                    cnt += 1

        # 4방향 모두 청소가 되어있을 때
        else:
            nr = r - dr[d]
            nc = c - dc[d]
            if 0 <= nr < height and 0 <= nc < width:
                if place[nr][nc]:
                    flag = True
                    break
                else:
                    r = nr
                    c = nc
                    cnt = 0
            else:
                flag = True
                break

print(sum(sum(clean[i]) for i in range(height)))

