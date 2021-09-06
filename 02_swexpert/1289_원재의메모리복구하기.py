for tc in range(int(input())):
    bit = list(map(int, input()))
    cnt = 0
    while sum(bit) != 0:
        # 1인 지점을 찾아 그 뒤를 모두 변경해준다.
        idx = bit.index(1)
        cnt += 1
        for i in range(idx, len(bit)):
            bit[i] = 1 - bit[i]
    print("#{} {}".format(tc+1, cnt))
    