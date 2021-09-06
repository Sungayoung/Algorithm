# 색종이
import pprint


paper = [[0] * 101 for _ in range(101)]

for _ in range(int(input())):
    x, y = map(int, input().split())

    for i in range(y, y+10):
        for j in range(x, x+10):
            paper[i][j] = 1

area = 0
for i in range(101):
    area += sum(paper[i])
print(area)