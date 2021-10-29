def find_idx(_num):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == _num:
                return i, j


for tc in range(10):
    input()
    maze = [list(map(int, input())) for _ in range(16)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    stack_list = []
    start = find_idx(2)
    stack_list.append(start)
    result = 0
    while stack_list and not result:
        cur = stack_list.pop()
        if maze[cur[0]][cur[1]] == 1:
            continue
        maze[cur[0]][cur[1]] = 1        # 방문했다는 표시
        for idx in range(4):
            temp_x = cur[1] + dx[idx]
            temp_y = cur[0] + dy[idx]

            if 0 <= temp_x < 16 and 0 <= temp_y < 16:
                if maze[temp_y][temp_x] == 0:
                    stack_list.append((temp_y, temp_x))
                elif maze[temp_y][temp_x] == 3:
                    result = 1
                    break

    print("#{} {}".format(tc+1, result))
