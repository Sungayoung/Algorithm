# 라면사기(Small)

N = int(input())
ramen = list(map(int, input().split())) + [0, 0]

money = 0
for i in range(N):
    if ramen[i + 1] <= ramen[i + 2]:
        min_cnt = min(ramen[i], ramen[i + 1], ramen[i + 2])
        money += 7 * min_cnt
        ramen[i] -= min_cnt
        ramen[i + 1] -= min_cnt
        ramen[i + 2] -= min_cnt

        min_cnt = min(ramen[i], ramen[i + 1])
        money += 5 * min_cnt
        ramen[i] -= min_cnt
        ramen[i + 1] -= min_cnt
    else:
        min_cnt = min(ramen[i], ramen[i + 1] - ramen[i + 2])
        money += 5 * min_cnt
        ramen[i] -= min_cnt
        ramen[i + 1] -= min_cnt

        min_cnt = min(ramen[i], ramen[i + 1], ramen[i + 2])
        money += 7 * min_cnt
        ramen[i] -= min_cnt
        ramen[i + 1] -= min_cnt
        ramen[i + 2] -= min_cnt

    money += ramen[i] * 3

print(money)
