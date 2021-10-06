# 드래곤 커브

def turn_90(_curve):
    global points
    # x, y의 방향을 이해가 편하게 바꿔줌
    c, r, d, g = _curve

    points.add((r, c))
    points.add((r + dr[d], c + dc[d]))

    # 원점을 기준으로 90도 회전 : (a, b) -> (-b, a)
    if g > 0:
        prev = [(r, c), (r + dr[d], c + dc[d])]
        for _ in range(g):
            center = prev[-1]
            for _i in range(len(prev) - 1, -1, -1):
                turn_r = (prev[_i][1] - center[1]) + center[0]
                turn_c = -(prev[_i][0] - center[0]) + center[1]
                prev.append((turn_r, turn_c))
                points.add((turn_r, turn_c))


dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

# 0: x, 1: y, 2: d, 3: g
dragon_curve = [list(map(int, input().split())) for _ in range(int(input()))]

points = set()
for curve in dragon_curve:
    turn_90(curve)
result = 0

for i in range(100):
    for j in range(100):
        if (i, j) in points and (i + 1, j) in points and (i, j + 1) in points and (i + 1, j + 1) in points:
            result += 1

print(result)
