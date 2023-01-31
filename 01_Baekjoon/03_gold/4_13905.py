# 세부
# 다익스트라

from collections import deque
import sys
input = sys.stdin.readline

house_cnt, bridge_cnt = map(int, input().split())

s_start, h_position = map(int, input().split())

# 0부터 시작하기 위해
s_start -= 1
h_position -= 1

graph = [[] for _ in range(house_cnt)]

for _ in range(bridge_cnt):
    h1, h2, k = map(int, input().split())
    graph[h1 - 1].append([h2 - 1, k])
    graph[h2 - 1].append([h1 - 1, k])

weight = [0] * house_cnt

q = deque()
q.append((s_start, 1000000))
weight[s_start] = 1000000
while q:
    c_v, c_k = q.popleft()
    if weight[c_v] > c_k:
        continue
    for n_v, n_k in graph[c_v]:
        min_weight = min(c_k, n_k)
        if weight[n_v] < min_weight:
            weight[n_v] = min_weight
            q.append((n_v, min_weight))

print(weight[h_position])
