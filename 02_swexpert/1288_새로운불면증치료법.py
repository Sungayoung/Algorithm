for tc in range(int(input())):
    N = int(input())
    num_set = set()
    idx = 1
    cnt = 0
    while len(num_set) < 10:
        num = N * idx
        while num > 0:
            num_set.add(num % 10)
            num //= 10
        cnt += 1
        idx += 1
    print("#{} {}".format(tc+1, cnt * N))