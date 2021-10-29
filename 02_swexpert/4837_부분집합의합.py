num_list = list(range(1, 13))

T = int(input())
for tc in range(T):
    result = 0
    set_len, set_sum = map(int, input().split())
    for bin_num in range(1 << 12):
        tmp = 0
        cnt = 0
        for j in range(12):
            if (1 << j) & bin_num:
                cnt += 1            # 부분집합의 갯수
                tmp += num_list[j]  # 부분집합의 합
        if cnt == set_len and tmp == set_sum:
            result += 1
    print("#{} {}".format(tc+1, result))
