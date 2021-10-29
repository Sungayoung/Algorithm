# 전기버스
def move_bus(idx, battery, change):
    global min_change

    # 베터리가 없을경우 return
    if battery < 0:
        return

    # 가지치기
    if change >= min_change:
        return

    if idx >= N:
        min_change = min(min_change, change)
        return

    # 현재 위치에서 베터리를 갈거나
    move_bus(idx + 1, station[idx] - 1, change + 1)

    # 갈지않거나
    move_bus(idx + 1, battery - 1, change)


for tc in range(int(input())):
    tmp = list(map(int, input().split()))

    N = tmp[0] - 1
    station = tmp[1:]
    min_change = 987654321
    move_bus(0, station[0], 0)
    print("#{} {}".format(tc + 1, min_change))
