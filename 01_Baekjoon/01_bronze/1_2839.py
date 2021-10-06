def sugar_count(sugar):
    flag = False
    min_cnt = 987654321

    for i in range(sugar // 5 + 1):
        cur_cnt = 0
        if (sugar - (i * 5)) % 3 == 0:
            # 한번이라도 나누어떨어지면 flag를 True로
            flag = True
            cur_cnt += i
            cur_cnt += (sugar - (i * 5)) // 3

            if cur_cnt < min_cnt:   # 최소값 갱신
                min_cnt = cur_cnt

    if flag:
        return min_cnt
    # 만약 flag가 False값 그대로라면 3, 5kg로 나누어떨어지지 않음
    else:
        return -1


# 봉지는 3kg, 5kg 두가지만 있음
sugar = int(input())
print(sugar_count(sugar))
