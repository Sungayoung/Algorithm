# 톱니바퀴

# N극 -> 0, S극 -> 1
wheel = [list(map(int, input())) for _ in range(4)]

head = [0] * 4

for _ in range(int(input())):
    wheel_idx, direction = map(int, input().split())
    same_wheel = [True] * 3
    q = []
    for i in range(3):
        # 같은 극인지 미리 판단
        if wheel[i][(head[i] + 2) % 8] != wheel[i + 1][(head[i + 1] - 2) % 8]:
            same_wheel[i] = False
    q.append((wheel_idx - 1, direction))
    visited = [False] * 4
    while q:
        cur_wheel, cur_dir = q.pop(0)
        visited[cur_wheel] = True
        head[cur_wheel] = (head[cur_wheel] - cur_dir) % 8
        for i in (-1, 1):
            n_wheel = cur_wheel + i
            if 0 <= n_wheel < 4:
                if not visited[n_wheel] and not same_wheel[(cur_wheel + n_wheel) // 2]:
                    q.append((n_wheel, -cur_dir))
result = 0
for i in range(4):
    result += (1 << i) * wheel[i][head[i]]

print(result)

# 0 1 2 3
#  0 1 2
