# 치킨배달


def comb(idx, sel):
    if sel == M:
        candidates.append(selected[:])
        return
    for i in range(idx, len(chicken)):
        selected[sel] = i
        comb(i + 1, sel + 1)


size, M = map(int, input().split())

# 0: 빈칸, 1: 집, 2: 치킨집
city = []
chicken = []
house = []
selected = [0] * M
for i in range(size):
    tmp = list(map(int, input().split()))
    for j in range(size):
        if tmp[j] == 1:
            house.append((i, j))
        elif tmp[j] == 2:
            chicken.append((i, j))
candidates = []

# 조합으로 치킨집 선택한 뒤 절대값으로 최단거리 구하기.
comb(0, 0)
min_dis = 987654321
for candidate in candidates:
    tmp_min_dis = 0
    # 모든집, 모든 치킨집에 관해 최소 거리를 구함.
    for h in house:
        tmp_dis = 987654321
        for j in range(M):
            tmp_dis = min(tmp_dis, abs(h[0] - chicken[candidate[j]][0]) + abs(h[1] - chicken[candidate[j]][1]))
        tmp_min_dis += tmp_dis
        if tmp_min_dis >= min_dis:
            break
    else:
        min_dis = min(min_dis, tmp_min_dis)

print(min_dis)
