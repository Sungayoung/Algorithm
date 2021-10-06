# 뱀
from collections import deque


def check_boundary(_r, _c):
    if 0 <= _r < size and 0 <= _c < size:
        return True
    else:
        return False


def snake(_r, _c):
    second = 0
    q = deque()
    q.append((_r, _c))
    d_idx = 0
    prev_second = 0
    for s, m in move:
        for i in range(int(s) - prev_second):
            second += 1
            tmp_r = q[0][0] + dr[d_idx]
            tmp_c = q[0][1] + dc[d_idx]
            if check_boundary(tmp_r, tmp_c):
                # 사과를 먹은 경우
                if (tmp_r, tmp_c) in apple:
                    q.appendleft((tmp_r, tmp_c))
                    apple.remove((tmp_r, tmp_c))
                # 내 몸에 닿은 경우
                elif (tmp_r, tmp_c) in q:
                    return second

                else:
                    q.pop()
                    q.appendleft((tmp_r, tmp_c))
            # 범위를 벗어난 경우
            else:
                return second
        prev_second = int(s)
        if m == "L":
            d_idx = (d_idx - 1) % 4
        elif m == "D":
            d_idx = (d_idx + 1) % 4


size = int(input())
apple = set()
for _ in range(int(input())):
    a_r, a_c = map(int, input().split())
    apple.add((a_r - 1, a_c - 1))
move = [input().split() for _ in range(int(input()))]

# 임의로 가장 마지막 지점을 넣어준다.
move.append([10000, "S"])
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

print(snake(0, 0))
