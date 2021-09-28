def solution(n, info):
    answer = []
    print(n)

    dp = [[0] * (n + 1) for _ in range(11)]
    for i in range(11):
        for j in range(n + 1):
            if j > info[i]:
                dp[i][j] = 10 - i
            elif info[i] and j <= info[i]:
                dp[i][j] = -(10 - i)
    print(dp)
    max_score = 0
    for idx_10 in range(n + 1):
        for idx_9 in range(n + 1):
            if idx_10 + idx_9 > n:
                continue
            for idx_8 in range(n + 1):
                if idx_10 + idx_9 + idx_8 > n:
                    continue
                for idx_7 in range(n + 1):
                    if idx_10 + idx_9 + idx_8 + idx_7 > n:
                        continue
                    for idx_6 in range(n + 1):
                        if idx_10 + idx_9 + idx_8 + idx_7 + idx_6 > n:
                            continue
                        for idx_5 in range(n + 1):
                            if idx_10 + idx_9 + idx_8 + idx_7 + idx_6 + idx_5 > n:
                                continue
                            for idx_4 in range(n + 1):
                                if idx_10 + idx_9 + idx_8 + idx_7 + idx_6 + idx_5 + idx_4 > n:
                                    continue
                                for idx_3 in range(n + 1):
                                    if idx_10 + idx_9 + idx_8 + idx_7 + idx_6 + idx_5 + idx_4 + idx_3 > n:
                                        continue
                                    for idx_2 in range(n + 1):
                                        if idx_10 + idx_9 + idx_8 + idx_7 + idx_6 + idx_5 + idx_4 + idx_3 + idx_2 > n:
                                            continue
                                        for idx_1 in range(n + 1):
                                            if idx_10 + idx_9 + idx_8 + idx_7 + idx_6 + idx_5 + idx_4 + idx_3 + idx_2 + idx_1 > n:
                                                continue
                                            for idx_0 in range(n + 1):
                                                if idx_0 + idx_1 + idx_2 + idx_3 + idx_4 + idx_5 + idx_6 + idx_7 + idx_8 + idx_9 + idx_10 == n:
                                                    new_list = [idx_10, idx_9, idx_8, idx_7, idx_6, idx_5, idx_4, idx_3, idx_2, idx_1, idx_0]
                                                    cur_score = 0
                                                    for idx in range(11):
                                                        cur_score += dp[idx][new_list[idx]]


                                                    if cur_score > max_score:
                                                        max_score = cur_score
                                                        answer = new_list[:]
                                                    elif cur_score == max_score and answer:
                                                        for idx in range(10, -1, -1):
                                                            if new_list[idx] > answer[idx]:
                                                                answer = new_list[:]
                                                                break
                                                            elif answer[idx] > new_list[idx]:
                                                                break

    if max_score == 0:
        return [-1]
    else:
        return answer


print(solution(10, [2,1,1,1,1,1,1,1,1,0,0]))
