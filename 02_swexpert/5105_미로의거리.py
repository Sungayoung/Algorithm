from myQ import Queue
import time
def find_index(_num):
    for _i in range(size + 2):
        for _j in range(size + 2):
            if maze[_i][_j] == _num:
                return _i, _j


def dfs(maze):
    visit_cnt = [[0] * (size + 2) for _ in range(size + 2)]
    # q = Queue()
    # q.enque(start)
    # while not q.empty():
    #     cur = q.deque()
    #     if maze[cur[0]][cur[1]] == 3:
    #         return visit_cnt[cur[0]][cur[1]] - 1
    #
    #     if maze[cur[0]][cur[1]] == 1:
    #         continue
    #     maze[cur[0]][cur[1]] = 1
    #     for i in range(4):
    #         temp_x = cur[1] + dx[i]
    #         temp_y = cur[0] + dy[i]
    #
    #         if maze[temp_y][temp_x] == 0 or maze[temp_y][temp_x] == 3:
    #             visit_cnt[temp_y][temp_x] = visit_cnt[cur[0]][cur[1]] + 1
    #             q.enque((temp_y, temp_x))
    q = []
    q.append(start)
    while len(q) > 0:
        cur = q.pop(0)
        if maze[cur[0]][cur[1]] == 3:
            return visit_cnt[cur[0]][cur[1]] - 1

        if maze[cur[0]][cur[1]] == 1:
            continue
        maze[cur[0]][cur[1]] = 1
        for i in range(4):
            temp_x = cur[1] + dx[i]
            temp_y = cur[0] + dy[i]

            if maze[temp_y][temp_x] == 0 or maze[temp_y][temp_x] == 3:
                visit_cnt[temp_y][temp_x] = visit_cnt[cur[0]][cur[1]] + 1
                q.append((temp_y, temp_x))
    return 0


for tc in range(int(input())):
    start_time = time.time()
    size = int(input())
    maze = [[1] * (size + 2)]
    maze.extend([[1] + list(map(int, input())) + [1] for _ in range(size)])
    maze.append([1] * (size + 2))

    start = find_index(2)
    dx = [-1, 1, 0, 0]  # 열
    dy = [0, 0, -1, 1]  # 행

    print("#{} {}".format(tc + 1, dfs(maze)))
    print(time.time() - start_time)
