# 셔틀런
def run(_dis):
    while _dis > 0:
        for i in range(1, 5):
            for j in range(1, i + 1):
                _dis -= 5
                if _dis <= 0:
                    return j
            for j in range(i, 0, -1):
                _dis -= 5
                if _dis < 0:
                    return j
                elif _dis == 0:
                    return j - 1


dis = int(input())

# 0, 1: 1-5, 2: 6-10, 3: 11-15, 4: 16-20

print(run(dis))
