for tc in range(int(input())):
    height, width = map(int, input().split())

    flag = [list(input()) for _ in range(height)]
    # W: 흰색, B: 파란색, R: 빨간색
    min_color = 987654321
    for w in range(1, height-1):
        for b in range(1, height-1):
            for r in range(1, height-1):
                if w+b+r == height:
                    tmp = 0
                    for i in range(0, w):
                        for j in range(width):
                            if flag[i][j] != "W":
                                tmp += 1
                    for i in range(w, w+b):
                        for j in range(width):
                            if flag[i][j] != "B":
                                tmp += 1
                    for i in range(w+b, height):
                        for j in range(width):
                            if flag[i][j] != "R":
                                tmp += 1
                    if tmp < min_color:
                        min_color = tmp

    print("#{} {}".format(tc+1, min_color))