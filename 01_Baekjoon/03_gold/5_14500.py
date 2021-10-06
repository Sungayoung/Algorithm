import sys

input = sys.stdin.readline


def check_boundary(_r, _c):
    if 0 <= _r < height and 0 <= _c < width:
        return True
    else:
        return False


tetrominos = [
    [(0, 1), (0, 2), (0, 3)],  # ㅡ
    [(1, 0), (2, 0), (3, 0)],  # ㅣ
    [(0, 1), (1, 0), (1, 1)],  # ㅁ
    [(1, 0), (2, 0), (2, 1)],  # ㄴ
    [(0, 1), (0, 2), (1, 2)],  # ㄱ
    [(1, 0), (2, 0), (2, -1)],  # 」
    [(1, 0), (1, 1), (1, 2)],  # ㄴ
    [(1, 0), (0, 1), (0, 2)],
    [(0, 1), (0, 2), (-1, 2)],
    [(1, 0), (2, 0), (0, 1)],
    [(0, 1), (1, 1), (2, 1)],
    [(1, 0), (1, 1), (2, 1)],  # ㄹ
    [(0, 1), (1, 1), (1, 2)],
    [(1, 0), (1, -1), (2, -1)],
    [(0, 1), (-1, 1), (-1, 2)],
    [(0, 1), (1, 1), (0, 2)],  # ㅜ
    [(1, 0), (1, 1), (2, 0)],  # ㅏ
    [(0, 1), (-1, 1), (0, 2)],  # ㅗ
    [(0, 1), (-1, 1), (1, 1)]  # ㅓ
]

height, width = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(height)]
max_num = 0
for i in range(height):
    for j in range(width):
        for tetromino in tetrominos:
            tmp_max = paper[i][j]
            for t in tetromino:
                try:
                    tmp_max += paper[i + t[0]][j + t[1]]
                except:
                    break
            max_num = max(max_num, tmp_max)

print(max_num)
