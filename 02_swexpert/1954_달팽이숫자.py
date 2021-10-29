# 달팽이 숫자

T = int(input())
for tc in range(T):
    size = int(input())
    dx = [1, 0, -1, 0]  # 가로방향
    dy = [0, 1, 0, -1]  # 세로방향
    snail = [[0] * size for _ in range(size)]
    d_idx = 0
    cur_x_pos = -1
    cur_y_pos = 0
    for num in range(1, size ** 2 + 1):
        temp_x = cur_x_pos + dx[d_idx]
        temp_y = cur_y_pos + dy[d_idx]

        # 범위 안에 있고 값이 할당되어있지 않다면
        if 0 <= temp_x < size and 0 <= temp_y < size and not snail[temp_y][temp_x]:
            snail[temp_y][temp_x] = num
            cur_x_pos = temp_x
            cur_y_pos = temp_y

        # 만약 범위를 벗어나거나 이미 값이 있다면 방향 인덱스를 하나 늘려줌
        else:
            d_idx = (d_idx + 1) % 4  # 인덱스 리스트의 길이는 항상 4로 고정, 나머지 이용
            cur_x_pos += dx[d_idx]
            cur_y_pos += dy[d_idx]
            snail[cur_y_pos][cur_x_pos] = num

    print("#{}".format(tc + 1))
    for s in snail:
        print(*s)
