# 색종이 붙이기

paper_cnt = {1: 5, 2: 5, 3: 5, 4: 5, 5: 5}
paper_size = {1: [], 2: [], 3: [], 4: [], 5: []}
paper = [list(map(int, input().split())) for _ in range(10)]

dr = [1, 0]
dc = [0, 1]

for i in range(10):
    for j in range(10):
        if paper[i][j]:
            for size in range(5):

                pass