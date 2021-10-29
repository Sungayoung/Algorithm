# 하나로
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
    cycle = DisjointSet(N - 1)
    edges.sort(key=lambda x: x[2])
    result = []
    idx = 0
    while len(result) < N - 1:
        st, ed, value = edges[idx]
        if cycle.find_set(st) != cycle.find_set(ed):
            cycle.union(st, ed)
            result.append(value)

        idx += 1

    answer = 0
    for num in result:
        answer += num * E

    return answer


for tc in range(int(input())):
    N = int(input())

    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())

    edges = []
    # 모든 섬을 연결하는 간선을 구함
    for i in range(N):
        for j in range(i + 1, N):
            dis = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
            edges.append((i, j, dis))
    print("#{} {}".format(tc + 1, round(kruskal())))
