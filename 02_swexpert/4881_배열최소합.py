def perm(idx, check):
    global min_num
    if idx == size:
        pass
        tmp = 0

        # 순열을 이용해 한줄에 하나씩만 읽어올 수 있도록 한다.
        for i in range(size):
            tmp += arr[i][sel[i]]
            if tmp > min_num:
                return
        if tmp < min_num:
            min_num = tmp
    for j in range(size):
        if check & (1 << j) == 0:
            sel[j] = idx
            perm(idx + 1, check | (1 << j))


for tc in range(int(input())):
    size = int(input())
    sel = [0] * size

    min_num = 987654321
    arr = [list(map(int, input().split())) for _ in range(size)]
    perm(0, 0)
    print("#{} {}".format(tc + 1, min_num))

