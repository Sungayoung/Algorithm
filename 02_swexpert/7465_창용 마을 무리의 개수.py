# 창용 마을 무리의 개수

def dfs(idx):
    s = [idx]
    while s:
        cur = s.pop()

        for _i in range(len(graph[cur])):
            n_v = graph[cur][_i]
            if not visited[n_v]:
                visited[n_v] = True
                s.append(n_v)


for tc in range(int(input())):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        st, ed = map(int, input().split())
        graph[st].append(ed)
        graph[ed].append(st)

    visited = [False] * (V + 1)
    cnt = 0
    for i in range(1, V + 1):
        if not visited[i]:
            cnt += 1
            visited[i] = True
            dfs(i)

    print("#{} {}".format(tc + 1, cnt))
