T = int(input())

for tc in range(T):
    part_str = input()
    total_str = input()

    part_str = set(part_str)
    max_cnt = 0
    for part in part_str:
        cnt = 0
        for s in total_str:
            if part == s:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    print("#{} {}".format(tc+1, max_cnt))