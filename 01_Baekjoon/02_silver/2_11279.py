# 최대 힙
import sys
import heapq

input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    num = int(input())
    if num == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    elif num > 0:
        heapq.heappush(heap, -num)
