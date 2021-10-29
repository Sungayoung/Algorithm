# 최소 이동 거리
from collections import deque


def dijkstra(start):
    distance = [987654321] * (V + 1)
    q = deque()
    q.append(start)
    distance[start] = 0
    while q:
        cur = q.popleft()

        for i in range(len(graph[cur])):
            end, value = graph[cur][i]

            if distance[end] > distance[cur] + value:
                distance[end] = distance[cur] + value
                q.append(end)
    return distance[V]


for tc in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        st, ed, val = map(int, input().split())

        graph[st].append((ed, val))

    print("#{} {}".format(tc+1, dijkstra(0)))
