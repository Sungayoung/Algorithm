# 상어초등학교

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

size = int(input())

student = {}

for _ in range(size ** 2):
    tmp = list(map(int, input().split()))
    student[tmp[0]] = tmp[1:]

classroom = [[0] * size for _ in range(size)]
for key, liked in student.items():
    empty_idx = []
    liked_idx = []
    max_empty = -1
    max_liked = -1
    for r in range(size):
        for c in range(size):
            if not classroom[r][c]:
                tmp_empty = 0
                tmp_liked = 0
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < size and 0 <= nc < size:
                        # 자리가 비어있는 경우
                        if not classroom[nr][nc]:
                            tmp_empty += 1
                        # 인접한 칸에 좋아하는 학생이 있는 경우
                        elif classroom[nr][nc] in liked:
                            tmp_liked += 1
                if tmp_empty > max_empty:
                    max_empty = tmp_empty
                    empty_idx = [r, c]

                # 인접한 칸에 좋아하는 학생이 가장 많은 칸이 여러개일 경우 빈칸이 가장 많은칸으로 자리 정한다.
                if tmp_liked > max_liked:
                    max_liked = tmp_liked
                    liked_idx = [tmp_empty, r, c]
                elif tmp_liked == max_liked:
                    if tmp_empty > liked_idx[0]:
                        liked_idx = [tmp_empty, r, c]

    if max_liked:
        classroom[liked_idx[1]][liked_idx[2]] = key
    else:
        classroom[empty_idx[0]][empty_idx[1]] = key

result = 0
for r in range(size):
    for c in range(size):
        liked_cnt = 0
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < size and 0 <= nc < size:
                if classroom[nr][nc] in student[classroom[r][c]]:
                    liked_cnt += 1
        if liked_cnt:
            result += 10 ** (liked_cnt - 1)

print(result)
