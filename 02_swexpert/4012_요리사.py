# 요리사

# 나눠진 두 그룹에서 2개씩 조합을 다시 구해 차이를 구함
def cal_diff(list_a, list_b):
    team_a = 0
    team_b = 0
    for i in range(N // 2):
        for j in range(i + 1, N // 2):
            team_a += synergy[list_a[i]][list_a[j]]
            team_a += synergy[list_a[j]][list_a[i]]
            team_b += synergy[list_b[i]][list_b[j]]
            team_b += synergy[list_b[j]][list_b[i]]
    return abs(team_a - team_b)


# 조합을 이용해 두 그룹으로 나놈
def comb(idx, sel):
    global min_diff

    if sel == N // 2:
        list_a = selected[:]
        list_b = list(set(range(N)) - set(list_a))
        min_diff = min(min_diff, cal_diff(list_a, list_b))
        return

    for i in range(idx, N):
        selected[sel] = i
        comb(i + 1, sel + 1)


for tc in range(int(input())):
    N = int(input())
    selected = [0] * (N // 2)
    min_diff = 987654321
    synergy = [list(map(int, input().split())) for _ in range(N)]
    comb(0, 0)
    print("#{} {}".format(tc + 1, min_diff))
