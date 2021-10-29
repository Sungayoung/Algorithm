# 연산

def cal_cnt(_num, _goal):
    num_list = [_num]
    flag = False
    visited = {_num}
    answer = 0
    while True:
        answer += 1
        new_list = []
        for num in num_list:

            # 더하기
            for i in range(3):
                tmp = num + op[i]
                if tmp == _goal:
                    return answer
                if 0 < tmp <= 1000000 and tmp not in visited:
                    visited.add(tmp)
                    new_list.append(tmp)

            # 곱하기
            tmp = num * 2
            if tmp == _goal:
                return answer
            if 0 < tmp <= 1000000 and tmp not in visited:
                visited.add(tmp)
                new_list.append(tmp)
        num_list = new_list[:]


for tc in range(int(input())):
    op = [1, -1, -10]
    N, goal = map(int, input().split())
    print("#{} {}".format(tc+1, cal_cnt(N, goal)))
