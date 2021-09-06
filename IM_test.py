for tc in range(int(input())):
    size = int(input())
    map_list = [list(input()) for _ in range(size)]
    # A: 1개 커버 기지국, B: 2개 커버 기지국, C: 3개 커버 기지국, H:Home

    for i in range(size):
        for j in range(size):
            cover_size = 0
            if map_list[i][j] == "A":
                cover_size = 1
            elif map_list[i][j] == "B":
                cover_size = 2
            elif map_list[i][j] == "C":
                cover_size = 3

            if cover_size:  # 기지국이 있어서 cover_size 에 값이 설정됐다면
                for l in range(-cover_size, cover_size + 1):
                    if 0 <= i + l < size and map_list[i + l][j] == "H":
                        map_list[i + l][j] = "X"  # 커버 가능한 집은 지워줌
                    if 0 <= j + l < size and map_list[i][j + l] == "H":
                        map_list[i][j + l] = "X"
    cnt = 0
    for i in range(size):
        cnt += map_list[i].count("H")
    print("#{} {}".format(tc + 1, cnt))
