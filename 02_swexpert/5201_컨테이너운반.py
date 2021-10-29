# 컨테이너 운반
for tc in range(int(input())):
    container_n, truck_n = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    result = 0
    for t in truck:
        max_idx = 0
        max_val = 0
        for w in range(len(weight)):
            if max_val < weight[w] <= t:
                max_idx = w
                max_val = weight[w]
        if max_val:
            result += weight[max_idx]

            # 최대값이 50이므로
            weight[max_idx] = 51
    print("#{} {}".format(tc+1, result))

