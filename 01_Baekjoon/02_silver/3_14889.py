# 스타트와 링크

def divide_team(idx, sel):
    if sel == size // 2:
        divided.append(selected[:])
        return

    for i in range(idx, size):
        if not visited[i]:
            selected[sel] = i
            visited[i] = True
            divide_team(i, sel + 1)
            visited[i] = False


def ability_sum(_num_list):
    _result = 0
    for _i in range(len(_num_list) - 1):
        for _j in range(_i + 1, len(_num_list)):
            _result += ability[_num_list[_i]][_num_list[_j]]
            _result += ability[_num_list[_j]][_num_list[_i]]

    return _result


size = int(input())
ability = [list(map(int, input().split())) for _ in range(size)]
selected = [0] * (size // 2)
visited = [False] * size
divided = []

divide_team(0, 0)
min_value = 987654321

for i in range(len(divided)):
    remain = []
    tmp_idx = 0
    for num in range(size):
        if tmp_idx >= size // 2:
            remain.append(num)
        else:
            if divided[i][tmp_idx] == num:
                tmp_idx += 1
            else:
                remain.append(num)
    start = ability_sum(divided[i])
    rink = ability_sum(remain)

    min_value = min(min_value, abs(start - rink))

print(min_value)
