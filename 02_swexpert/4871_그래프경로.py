def DFS(_start, _end):
    Stack_list = []
    Stack_list.append(_start)
    while Stack_list:
        cur = Stack_list.pop()

        # 만약 도착지점을 방문했다면
        if cur == _end:
            return 1
        if visited[cur]:
            continue

        visited[cur] = True
        for _i in range(len(V_list[cur])):
            if not visited[V_list[cur][_i]]:
                Stack_list.append(V_list[cur][_i])
    return 0


T = int(input())

for tc in range(T):
    V, E = map(int, input().split())

    V_list = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    for i in range(E):
        st, ed = map(int, input().split())
        V_list[st].append(ed)
    start, end = map(int, input().split())
    print("#{} {}".format(tc+1, DFS(start, end)))
