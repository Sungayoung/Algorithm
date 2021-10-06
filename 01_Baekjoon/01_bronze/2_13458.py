# 시험감독
import math
import sys
input = sys.stdin.readline

N = int(input())  # 시험장의 갯수
people = list(map(int, input().split()))
main, sub = map(int, input().split())  # 총 감독관, 부 감독관

cnt = 0
for p in people:
    p -= main
    cnt += 1
    if p > 0:
        cnt += math.ceil(p / sub)

print(cnt)
