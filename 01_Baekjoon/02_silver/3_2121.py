import sys

# 넷이 놀기

N = int(sys.stdin.readline())
width, height = map(int, sys.stdin.readline().split())
point_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
point_set = set(point_list)

result = 0
for p in range(N):
    x = point_list[p][0]
    y = point_list[p][1]
    if (x + width, y + height) in point_set and (x + width, y) in point_set and (x, y + height) in point_set:
        result += 1
print(result)
