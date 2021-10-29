# 최소 신장 트리
class DisjointSet:

    def __init__(self, n):
        self.p = list(range(n + 1))

    def find_set(self, x):
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])

        return self.p[x]

    def union(self, a, b):
        self.p[self.find_set(b)] = self.find_set(a)


def kruskal():
    cycle = DisjointSet(V)
    copy_graph = sorted(kruskal_graph, key=lambda x: x[2])
    distance = []
    idx = 0
    while len(distance) < V:
        if cycle.find_set(copy_graph[idx][0]) != cycle.find_set(copy_graph[idx][1]):
            distance.append(copy_graph[idx][2])
            cycle.union(copy_graph[idx][0], copy_graph[idx][1])
        idx += 1
    return sum(distance)


def prim():
    distance = [987654321] * (V + 1)
    prev = [0] * (V + 1)
    visited = [False] * (V + 1)
    cur = 0
    distance[0] = 0
    for _ in range(V + 1):
        if visited[cur]:
            continue
        visited[cur] = True

        for i in range(len(prim_graph[cur])):
            end, value = prim_graph[cur][i]

            if not visited[end] and distance[end] > value:
                prev[end] = cur
                distance[end] = value

        min_dis = 987654321

        for i in range(V + 1):
            if not visited[i] and distance[i] < min_dis:
                min_dis = distance[i]
                cur = i

    return sum(distance)


for tc in range(int(input())):
    V, E = map(int, input().split())

    kruskal_graph = [list(map(int, input().split())) for _ in range(E)]
    prim_graph = [[] for _ in range(V + 1)]

    for info in kruskal_graph:
        st, ed, v = info
        prim_graph[st].append((ed, v))
        prim_graph[ed].append((st, v))
    result = prim()
    # result = kruskal()
    print("#{} {}".format(tc + 1, result))
