# 참외밭

# K: 참외의 갯수
K = int(input())
# 1:동, 2:서, 3:남, 4:북

field = [tuple(map(int, input().split())) for _ in range(6)]

max_height = 0
max_width = 0
max_height_idx = 0
max_width_idx = 0
for i in range(6):
    if field[i][0] == 1 or field[i][0] == 2:
        if field[i][1] > max_height:
            max_height = field[i][1]
            max_height_idx = i
    else:
        if field[i][1] > max_width:
            max_width = field[i][1]
            max_width_idx = i

s_area = abs(field[(max_width_idx - 1) % 6][1] - field[(max_width_idx + 1) % 6][1]) * abs(
    field[(max_height_idx - 1) % 6][1] - field[(max_height_idx + 1) % 6][1])
area = max_width * max_height - s_area
print(area * K)
