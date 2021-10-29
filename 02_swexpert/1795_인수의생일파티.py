# 인수의 생일파티
from collections import deque


def dijkstra(idx, _graph):
    distance = [987654321] * V
    q = deque()
    q.append(idx)
    distance[idx] = 0
    while q:
        cur = q.popleft()

        for i in range(len(_graph[cur])):
            _end, _value = _graph[cur][i]

            if distance[_end] > distance[cur] + _value:
                distance[_end] = distance[cur] + _value
                q.append(_end)
    return distance[:]


for tc in range(int(input())):
    V, E, X = map(int, input().split())

    graph = [[] for _ in range(V)]
    reversed_graph = [[] for _ in range(V)]
    for _ in range(E):
        st, ed, value = map(int, input().split())

        graph[st - 1].append((ed - 1, value))
        reversed_graph[ed - 1].append((st - 1, value))

    result = [0] * V

    tmp_list = dijkstra(X - 1, graph)
    for i in range(V):
        result[i] += tmp_list[i]
    tmp_list = dijkstra(X - 1, reversed_graph)
    for i in range(V):
        result[i] += tmp_list[i]

    print("#{} {}".format(tc + 1, max(result)))
