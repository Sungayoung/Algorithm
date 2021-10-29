# 쉬운 거스름돈

for tc in range(int(input())):
    change = {
        50000: 0, 10000: 0,
        5000: 0,  1000: 0,
        500: 0,   100: 0,
        50: 0,    10: 0
    }

    money = int(input())

    for key in change.keys():
        change[key] += money // key
        money %= key

    print("#{}".format(tc+1))
    print(*change.values())