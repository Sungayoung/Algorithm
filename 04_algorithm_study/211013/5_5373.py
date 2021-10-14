# 큐빙

# 큐브 번호와 행, 열 인덱스
direction = {
    'U': [1, (0, [0, 2], [0, 1], [0, 0]), (2, [0, 2], [0, 1], [0, 0]), (5, [2, 0], [2, 1], [2, 2]),
          (3, [0, 2], [0, 1], [0, 0])],
    'D': [4, (0, [2, 0], [2, 1], [2, 2]), (3, [2, 0], [2, 1], [2, 2]), (5, [0, 2], [0, 1], [0, 0]),
          (2, [2, 0], [2, 1], [2, 2])],
    'F': [0, (1, [2, 0], [2, 1], [2, 2]), (3, [0, 0], [1, 0], [2, 0]), (4, [0, 2], [0, 1], [0, 0]),
          (2, [2, 2], [1, 2], [0, 2])],
    'B': [5, (1, [0, 2], [0, 1], [0, 0]), (2, [0, 0], [1, 0], [2, 0]), (4, [2, 0], [2, 1], [2, 2]),
          (3, [2, 2], [1, 2], [0, 2])],
    'L': [2, (1, [0, 0], [1, 0], [2, 0]), (0, [0, 0], [1, 0], [2, 0]), (4, [0, 0], [1, 0], [2, 0]),
          (5, [0, 0], [1, 0], [2, 0])],
    'R': [3, (5, [2, 2], [1, 2], [0, 2]), (4, [2, 2], [1, 2], [0, 2]), (0, [2, 2], [1, 2], [0, 2]),
          (1, [2, 2], [1, 2], [0, 2])]
}

# U: 윗 면, D: 아랫 면, F: 앞 면, B: 뒷 면, L: 왼쪽 면, R: 오른쪽 면
# 0: 빨간색, 1: 흰색, 2: 초록색, 3: 파란색, 4: 노란색, 5: 오렌지색
for tc in range(int(input())):
    N = int(input())
    commands = input().split()
    colors = ['r', 'w', 'g', 'b', 'y', 'o']
    cube = []
    for color in colors:
        tmp = [[color] * 3 for _ in range(3)]
        cube.append(tmp)

    for command in commands:
        tmp_line = []
        change_list = direction[command[0]][1:]

        for change in change_list:
            for idx in range(1, 4):
                tmp_line.append(cube[change[0]][change[idx][0]][change[idx][1]])

        way = 1
        if command[1] == '-':
            way = 3

        # 다른 면과 값이 바뀌는 부분
        for i in range(4):
            goal = change_list[(i + way) % 4]
            for idx in range(3):
                cube[goal[0]][goal[idx + 1][0]][goal[idx + 1][1]] = tmp_line[i * 3 + idx]

        side = direction[command[0]][0]
        # 한면만 회전
        for _ in range(way):
            new_cube = [[""] * 3 for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    new_cube[i][j] = cube[side][2 - j][i]

            cube[side] = new_cube

    for i in range(3):
        for j in range(3):
            print(cube[1][i][j], end="")
        print()
