# 0: 현재 속도 유지, 1: 가속, 2: 감속

for tc in range(int(input())):
    dis = 0
    N = int(input())
    cur_velocity = 0
    for _ in range(N):
        tmp = list(map(int, input().split()))
        if tmp[0] == 1:
            cur_velocity += tmp[1]
        elif tmp[0] == 2:
            cur_velocity = 0 if cur_velocity - tmp[1] <= 0 else cur_velocity - tmp[1]
        dis += cur_velocity
    print("#{} {}".format(tc+1, dis))