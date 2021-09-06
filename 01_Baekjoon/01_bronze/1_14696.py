# 딱지놀이

def who_win(_list1, _list2):
    for _i in range(3, -1, -1):
        if _list1[_i] > _list2[_i]:
            return "A"
        elif _list1[_i] < _list2[_i]:
            return "B"
    return "D"


N = int(input())

for _ in range(N):
    paper1 = [0] * 4
    paper2 = [0] * 4

    tmp1 = list(map(int, input().split()))
    tmp2 = list(map(int, input().split()))

    for i in range(1, tmp1[0] + 1):
        paper1[tmp1[i] - 1] += 1
    for i in range(1, tmp2[0] + 1):
        paper2[tmp2[i] - 1] += 1
    print(who_win(paper1, paper2))
