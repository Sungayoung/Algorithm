max_diff = 0
lion_info = [0] * 11
apeach_info = []
tmp_answer = []


def recursion(idx, count, n):
    global max_diff
    global tmp_answer
    if idx == 11:
        if count == n:
            apeach = 0
            lion = 0
            for i in range(11):
                if apeach_info[i] > 0 or lion_info[i] > 0:
                    if apeach_info[i] >= lion_info[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i

            if max_diff < lion - apeach:
                max_diff = lion - apeach
                tmp_answer = lion_info[:]
            elif max_diff == lion - apeach and lion - apeach > 0 and tmp_answer:
                for i in range(10, -1, -1):
                    if tmp_answer[i] < lion_info[i]:
                        tmp_answer = lion_info[:]
                        break
                    elif tmp_answer[i] > lion_info[i]:
                        break

        return

    for c in range(count, n+1):
        lion_info[idx] = c - count
        recursion(idx + 1, c, n)
        lion_info[idx] = 0


def solution(n, info):
    global apeach_info
    apeach_info = info[:]

    recursion(0, 0, n)
    if max_diff == 0:
        return [-1]
    return tmp_answer
