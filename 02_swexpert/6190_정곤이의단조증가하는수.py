for tc in range(int(input())):
    N = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort(reverse=True)

    max_num = 0
    cnt = 0
    flag = True
    for i in range(N-1):
        for j in range(i+1, N):
            num = num_list[i] * num_list[j]
            prev = 9
            while num > 0:
                if num % 10 > prev:
                    break
                prev = num % 10
                num //= 10
            else:
                tmp = num_list[i] * num_list[j]
                if tmp > max_num:
                    max_num = tmp
                    flag = False
    if flag:
        max_num = -1
    print("#{} {}".format(tc+1, max_num))