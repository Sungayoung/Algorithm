def is_in_boundary(position_y, position_x):
    if 0 <= position_y < height and 0 <= position_x < width:
        return True
    else:
        return False


height, width = map(int, input().split())

maze = [list(map(int, input())) for _ in range(height)]
distance = [[0] * width for _ in range(height)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = []
start = (0, 0)
end = (height - 1, width - 1)
queue.append(start)
distance[start[0]][start[1]] = 1

while queue:
    cur_pos = queue.pop(0)
    if maze[cur_pos[0]][cur_pos[1]] == 0:
        continue
    maze[cur_pos[0]][cur_pos[1]] = 0
    for idx in range(4):
        temp_y = cur_pos[0] + dy[idx]
        temp_x = cur_pos[1] + dx[idx]

        if is_in_boundary(temp_y, temp_x) and maze[temp_y][temp_x]:
            queue.append((temp_y, temp_x))
            distance[temp_y][temp_x] = distance[cur_pos[0]][cur_pos[1]] + 1

print(distance[height-1][width-1])
