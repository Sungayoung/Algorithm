# 작업 순서
def topological_sort():
    idx = 0
    q = []
    for _i in range(1, V + 1):
        if in_cnt[_i] == 0:
            q.append(_i)

    while idx < V:
        cur = q[idx]

        for i in range(len(graph[cur])):
            n_v = graph[cur][i]
            in_cnt[n_v] -= 1
            if in_cnt[n_v] == 0:
                q.append(n_v)
        idx += 1
    return q



for tc in range(10):
    V, E = map(int, input().split())

    line = list(map(int, input().split()))
    in_cnt = [0] * (V + 1)
    out_cnt = [0] * (V + 1)
    graph = [[] for _ in range(V + 1)]
    for i in range(E):
        graph[line[i * 2]].append(line[i * 2 + 1])
        out_cnt[line[i * 2]] += 1
        in_cnt[line[i * 2 + 1]] += 1
    # result = topological_sort()

    print("#{}".format(tc+1), end=" ")
    print(*topological_sort())
