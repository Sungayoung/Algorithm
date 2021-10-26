# ACM Craft

for tc in range(int(input())):
    V, E = map(int, input().split())
    in_cnt = [0] * V
    second = list(map(int, input().split()))

    graph = [[] for _ in range(V)]
    for _ in range(E):
        st, ed = map(int, input().split())
        graph[st - 1].append(ed - 1)
        in_cnt[ed - 1] += 1
    goal = int(input())
    q = []
    time = [0] * V
    for i in range(V):
        if in_cnt[i] == 0:
            q.append(i)
            time[i] = second[i]

    idx = 0
    visited = [False] * V
    while idx < len(q):
        cur = q[idx]
        visited[cur] = True

        for i in range(len(graph[cur])):
            nv = graph[cur][i]

            time[nv] = max(time[nv], time[cur] + second[nv])
            in_cnt[nv] -= 1
            if in_cnt[nv] == 0:
                q.append(nv)
        idx += 1
    print(time[goal-1])
