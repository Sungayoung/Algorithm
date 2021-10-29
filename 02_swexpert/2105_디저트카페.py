# 디저트카페

dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

for tc in range(int(input())):
    size = int(input())
    cafe = [list(map(int, input().split())) for _ in range(size)]

    max_dessert = -1
    for r in range(size - 2):
        for c in range(1, size - 1):
            # 정점을 기준으로 오른쪽 대각선 길이
            for d1 in range(1, size - c):
                # 정점을 기준으로 왼쪽 대각선 길이
                for d2 in range(1, c + 1):
                    if r + d1 + d2 >= size:
                        continue

                    # 먹은 디저트를 저장할 set
                    dessert_set = set()
                    flag = False
                    cur_r, cur_c = r, c
                    for d in range(4):
                        if d % 2:
                            length = d2
                        else:
                            length = d1
                        for l in range(1, length + 1):
                            cur_r += dr[d]
                            cur_c += dc[d]
                            if cafe[cur_r][cur_c] in dessert_set:
                                flag = True
                                break
                            dessert_set.add(cafe[cur_r][cur_c])
                        if flag:
                            break
                    # 중간에 break 되지않고 다시 자기자리로 돌아왔다면
                    else:
                        max_dessert = max(max_dessert, len(dessert_set))

    print("#{} {}".format(tc+1, max_dessert))
