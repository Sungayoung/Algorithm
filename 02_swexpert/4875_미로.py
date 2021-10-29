for tc in range(int(input())):
    size = int(input())
    maze = [[1] * (size + 2)]
    for _ in range(size):
        maze.append([1] + list(map(int, input().strip())) + [1])
    maze.append([1] * (size + 2))
    stack = []
    start_idx = (0, 0)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(size + 2):
        for j in range(size + 2):
            if maze[i][j] == 2:
                start_idx = (i, j)
                maze[i][j] = 0

    result = 0
    stack.append(start_idx)
    while stack:
        cur = stack.pop()
        if maze[cur[0]][cur[1]]:
            continue
        maze[cur[0]][cur[1]] = 1

        for idx in range(4):
            tmp_x = cur[1] + dx[idx]
            tmp_y = cur[0] + dy[idx]
            if maze[tmp_y][tmp_x] == 0:
                stack.append((tmp_y, tmp_x))
            elif maze[tmp_y][tmp_x] == 3:
                result = 1
                break
    print("#{} {}".format(tc + 1, result))