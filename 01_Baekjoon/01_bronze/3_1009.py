for tc in range(1, int(input()) + 1):
    # N : 정수 개수, M : 구간의 개수
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    # 초기값 세팅
    tmp = 0
    for i in range(M):
        tmp += nums[i]
    print(tmp)
    max_value = min_value = tmp
    #중복연산을 하지 않음
    for i in range(M, N):
        tmp = tmp + nums[i] - nums[i - M]
        print(tmp)

        if max_value < tmp:
            max_value = tmp
        if min_value > tmp:
            min_value = tmp

    print("#{} {}".format(tc, max_value - min_value))