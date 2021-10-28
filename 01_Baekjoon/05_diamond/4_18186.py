# 라면사기 (large)

N, B, C = map(int, input().split())
ramen = list(map(int, input().split())) + [0, 0]

money = 0
if B < C:
    for i in range(N):
        money += B * ramen[i]
else:
    for i in range(N):
        if ramen[i + 1] <= ramen[i + 2]:
            min_cnt = min(ramen[i], ramen[i + 1], ramen[i + 2])
            money += (B + 2 * C) * min_cnt
            ramen[i] -= min_cnt
            ramen[i + 1] -= min_cnt
            ramen[i + 2] -= min_cnt

            min_cnt = min(ramen[i], ramen[i + 1])
            money += (B + C) * min_cnt
            ramen[i] -= min_cnt
            ramen[i + 1] -= min_cnt
        else:
            min_cnt = min(ramen[i], ramen[i + 1] - ramen[i + 2])
            money += (B + C) * min_cnt
            ramen[i] -= min_cnt
            ramen[i + 1] -= min_cnt

            min_cnt = min(ramen[i], ramen[i + 1], ramen[i + 2])
            money += (B + 2 * C) * min_cnt
            ramen[i] -= min_cnt
            ramen[i + 1] -= min_cnt
            ramen[i + 2] -= min_cnt

        money += ramen[i] * B

print(money)
