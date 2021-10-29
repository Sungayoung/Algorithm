def bfs():
    visit_cnt = [0] * (V + 1)
    q = [start]
    # visit_cnt[start] = 0
    while len(q) > 0:
        cur = q.pop(0)
        for _i in range(len(vertex[cur])):
            next_v = vertex[cur][_i]
            if next_v == goal:
                return visit_cnt[cur] + 1

            if visit_cnt[next_v] == 0:
                visit_cnt[next_v] = visit_cnt[cur] + 1
                q.append(next_v)
    return 0


for tc in range(int(input())):

    V, E = map(int, input().split())
    vertex = [[] for _ in range(V + 1)]
    for _ in range(E):
        st, ed = map(int, input().split())
        vertex[st].append(ed)
        vertex[ed].append(st)
    start, goal = map(int, input().split())
    print("#{} {}".format(tc+1, bfs()))
