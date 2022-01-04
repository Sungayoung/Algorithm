# 시계 사진들
from collections import deque

N = int(input())

clock_1 = list(map(int, input().split()))
clock_2 = list(map(int, input().split()))

clock_1_list = deque([0] * 360000)
clock_2_list = deque([0] * 360000)

for i in range(N):
    clock_1_list[clock_1[i]] = 1
    clock_2_list[clock_2[i]] = 1

ans = 'impossible'
for _ in range(360000):
    for i in range(360000):
        if clock_1_list[i] != clock_2_list[i]:
            break
    else:
        ans = 'possible'
        break

    clock_2_list.rotate(1)
print(ans)
