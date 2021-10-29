def who_win(idx_1, idx_2):
    # 1: 가위, 2: 바위, 3: 보
    if card[idx_1] - card[idx_2] == 1 or card[idx_1] - card[idx_2] == -2:
        return idx_1
    elif card[idx_1] == card[idx_2]:
        return idx_1
    else:
        return idx_2
    pass


def merge_sort(_start, _end):
    _mid = (_start + _end) // 2
    if _start == _end:
        return _start
    elif _end - _start == 1:
        return who_win(_start, _end)

    # 양쪽을 분할해서 이기는 쪽을 리턴한다
    return who_win(merge_sort(_start, _mid), merge_sort(_mid + 1, _end))


for tc in range(int(input())):
    N = int(input())
    card = list(map(int, input().split()))
    start = 0
    end = N - 1
    tournament = list(range(N))
    print("#{} {}".format(tc + 1, merge_sort(start, end) + 1))
