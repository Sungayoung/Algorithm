# 좌표 정렬하기
import sys

input = sys.stdin.readline
N = int(input())
points = []
for _ in range(N):
    points.append(list(map(int, input().split())))

points.sort()
for i in range(N):
    print(f"{points[i][0]} {points[i][1]}")