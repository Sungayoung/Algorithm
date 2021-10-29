# 이진수 2

for tc in range(int(input())):
    goal = float(input())
    result = ''
    cur_num = 0
    for i in range(12):
        float_num = 1 / (2 << i)
        if goal < cur_num + float_num:
            result += '0'
        elif goal > cur_num + float_num:
            cur_num += float_num
            result += '1'
        else:
            result += '1'
            break
    else:
        result = 'overflow'

    print("#{} {}".format(tc + 1, result))
