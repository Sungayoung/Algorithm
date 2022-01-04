# 가운데를 말해요
import sys
import heapq

input = sys.stdin.readline

max_heap = []
min_heap = []

for i in range(int(input())):
    num = int(input())

    if len(max_heap) == 0:
        heapq.heappush(max_heap, -num)
    else:
        small_num = -max_heap[0]

        if num <= small_num:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        if len(max_heap) < len(min_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        elif len(max_heap) - len(min_heap) > 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

    print(-max_heap[0])
