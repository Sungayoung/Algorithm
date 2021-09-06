max_y, max_x = tuple(map(int, input().split()))

campus = []
x_pos = 0
y_pos = 0
queue = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(max_y):
    campus.append(list(input()))
    if 'I' in campus[i]:
        x_pos = campus[i].index('I')
        y_pos = i

cnt = 0
queue.append((x_pos, y_pos))
campus[y_pos][x_pos] = "V"
while len(queue) > 0:
    cur_x, cur_y = queue.pop(0)
    # print(cur_x, cur_y)
    # print(campus[cur_y][cur_x])
    for idx in range(4):
        temp_x = cur_x + dx[idx]
        temp_y = cur_y + dy[idx]
        # print(f"temp {temp_x}, {temp_y}")
        if 0 <= temp_x < max_x and 0 <= temp_y < max_y:
            if campus[temp_y][temp_x] == "O":
                queue.append((temp_x, temp_y))
                campus[temp_y][temp_x] = "V"
            elif campus[temp_y][temp_x] == "P":
                queue.append((temp_x, temp_y))
                campus[temp_y][temp_x] = "V"
                cnt += 1

if cnt == 0:
    print("TT")
else:
    print(cnt)
