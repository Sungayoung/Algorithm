for tc in range(int(input())):
    num_len, cnt = map(int, input().split())
    num_list = list(map(int, input().split()))
    print("#{} {}".format(tc+1, num_list[cnt % num_len]))