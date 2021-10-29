# 장훈이의 높은 선반

for tc in range(int(input())):
    N, H = map(int, input().split())

    height = list(map(int, input().split()))

    min_height = 987654321

    for i in range(2 << N - 1):
        tmp_height = 0
        for j in range(N):
            if i & 1 << j:
                tmp_height += height[j]
                if tmp_height >= min_height:
                    break
        else:
            if tmp_height >= H:
                min_height = min(min_height, tmp_height)

    print("#{} {}".format(tc+1, min_height - H))

