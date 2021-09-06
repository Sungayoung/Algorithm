# 계란으로 계란치기
# 순열 재귀 응용
def max_egg_cnt(idx, _egg_dur):
    global max_broken_egg

    if idx == N:
        cnt = 0
        # print(_egg_dur)
        for egg in _egg_dur:
            if egg <= 0:
                cnt += 1
        if cnt > max_broken_egg:
            max_broken_egg = cnt
        return
    # 이미 깨진계란이면 다음계란으로 넘어감
    if _egg_dur[idx] <= 0:
        max_egg_cnt(idx + 1, _egg_dur[:])
    else:
        flag = True  # 깨지지 않은 다른 계란이 없으면 치지 않고 넘어감
        for _i in range(N):
            if _egg_dur[_i] > 0 and idx != _i:
                flag = False
                # 깨고
                _egg_dur[_i] -= egg_weight[idx]
                _egg_dur[idx] -= egg_weight[_i]
                max_egg_cnt(idx + 1, _egg_dur[:])
                # 원상복구
                _egg_dur[_i] += egg_weight[idx]
                _egg_dur[idx] += egg_weight[_i]
        if flag:
            max_egg_cnt(idx+1, _egg_dur[:])


# 0: 내구도, 1: 무게

N = int(input())

egg_dur = []
egg_weight = []
for _ in range(N):
    tmp = tuple(map(int, input().split()))
    egg_dur.append(tmp[0])
    egg_weight.append(tmp[1])
max_broken_egg = 0
max_egg_cnt(0, egg_dur[:])
print(max_broken_egg)
