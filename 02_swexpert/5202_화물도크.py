# 화물도크
for tc in range(int(input())):
    N = int(input())

    time_table = []
    for idx in range(N):
        start, end = map(int, input().split())
        time_table.append((start, end))
    max_value = 0
    time_table.sort(key=lambda x: (x[1], x[0]))
    end_time = 0
    for i in range(len(time_table)):
        if time_table[i][0] >= end_time:
            end_time = time_table[i][1]
            max_value += 1
    print("#{} {}".format(tc+1, max_value))