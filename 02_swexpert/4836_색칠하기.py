T = int(input())

for tc in range(T):
    image = [[0] * 10 for _ in range(10)]
    color_len = int(input())
    color_cnt = 0
    for _ in range(color_len):
        y1, x1, y2, x2, color = map(int, input().split())

        # 같은 색은 겹치지 않는다 했으니 따로 값을 점검하지 않고 더해줌
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                image[y][x] += 1

    for i in range(10):
        for j in range(10):
            # 만약 두가지색이 겹쳤다면
            if image[i][j] >= 2:
                color_cnt += 1

    print("#{} {}".format(tc + 1, color_cnt))
