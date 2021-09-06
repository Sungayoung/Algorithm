# 직사각형 네개의 합집합의 면적 구하기

plane = [[0] * 101 for _ in range(101)]

for _ in range(4):
    point = list(map(int, input().split()))

    for y in range(point[1], point[3]):
        for x in range(point[0], point[2]):
            plane[y][x] = 1

num_sum = 0
for i in range(101):
    num_sum += sum(plane[i])
print(num_sum)