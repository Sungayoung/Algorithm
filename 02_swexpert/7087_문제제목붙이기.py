for tc in range(int(input())):

    N = int(input())
    tmp = [input()[0] for _ in range(N)]
    alpha_list = list(set(tmp))
    alpha_list.sort()
    start = 65
    cnt = 0
    for alpha in alpha_list:
        if alpha == chr(start):
            cnt += 1
            start += 1
        else:
            break
    print("#{} {}".format(tc+1, cnt))