# 사다리조작
import sys

input = sys.stdin.readline


def ladder():
    for i in range(1, height + 1):
        level = 0
        cur_pos = i
        while level < width:
            if is_connected[level][(cur_pos * 2 - 1) // 2]:
                cur_pos -= 1
            elif is_connected[level][(cur_pos * 2 + 1) // 2]:
                cur_pos += 1
            level += 1
        if i != cur_pos:
            return False
    return True


# height: 세로선의 개수, width: 가로선의 개수
height, H, width = map(int, input().split())

# 양 끝점을 고려해주기 위해
is_connected = [[False] * (height + 1) for _ in range(width)]

for _ in range(H):
    a, b = map(int, input().split())

    is_connected[a - 1][b] = True
V = (height - 1) * width

min_cnt = 987654321

# 사다리를 하나도 안세워도 되는 경우
if ladder():
    min_cnt = 0

if min_cnt:
    for a in range(V):
        w1 = a // (height - 1)
        h1 = a % (height - 1) + 1
        if is_connected[w1][h1] or is_connected[w1][h1 - 1] or is_connected[w1][h1 + 1]:
            continue
        is_connected[w1][h1] = True
        if ladder():
            min_cnt = 1
            break

        if min_cnt == 2:
            is_connected[w1][h1] = False
            continue
        for b in range(a + 1, V):
            w2 = b // (height - 1)
            h2 = b % (height - 1) + 1
            if is_connected[w2][h2] or is_connected[w2][h2 - 1] or is_connected[w2][h2 + 1]:
                continue
            is_connected[w2][h2] = True
            if ladder():
                min_cnt = min(min_cnt, 2)

            if min_cnt == 3:
                is_connected[w2][h2] = False
                continue

            for c in range(b + 1, V):
                w3 = c // (height - 1)
                h3 = c % (height - 1) + 1
                if is_connected[w3][h3] or is_connected[w3][h3 - 1] or is_connected[w3][h3 + 1]:
                    continue
                is_connected[w3][h3] = True
                if ladder():
                    min_cnt = min(min_cnt, 3)

                # 원상복구
                is_connected[w3][h3] = False
            is_connected[w2][h2] = False
        is_connected[w1][h1] = False

if min_cnt == 987654321:
    min_cnt = -1

print(min_cnt)
