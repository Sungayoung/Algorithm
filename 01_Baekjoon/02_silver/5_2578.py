# 빙고
bingo_list = [list(map(int, input().split())) for _ in range(5)]
bingo_dict = {}
for i in range(5):
    for j in range(5):
        bingo_dict[bingo_list[i][j]] = (i, j)
MC = []
for _ in range(5):
    MC.extend(list(map(int, input().split())))

horizon = [0] * 5
vertical = [0] * 5
digonal = [0] * 2
bingo_cnt = 0
result = 0

for idx, num in enumerate(MC):
    r, c = bingo_dict[num]
    horizon[r] += 1
    if horizon[r] == 5:
        bingo_cnt += 1
    vertical[c] += 1
    if vertical[c] == 5:
        bingo_cnt += 1
    if r == c:
        digonal[0] += 1
        if digonal[0] == 5:
            bingo_cnt += 1
    if r + c == 4:
        digonal[1] += 1
        if digonal[1] == 5:
            bingo_cnt += 1

    if bingo_cnt >= 3:
        print(idx + 1)
        break
