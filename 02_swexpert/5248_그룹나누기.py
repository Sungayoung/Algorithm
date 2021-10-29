# 그룹 나누기
def dfs(idx):
    s = [idx]

    while s:
        cur = s.pop()

        for _i in range(len(graph[cur])):
            if not visited[graph[cur][_i]]:
                visited[graph[cur][_i]] = True
                s.append(graph[cur][_i])


for tc in range(int(input())):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    line = list(map(int, input().split()))
    for i in range(M):
        graph[line[i * 2]].append(line[i * 2 + 1])
        graph[line[i * 2 + 1]].append(line[i * 2])
    visited = [False] * (N + 1)

    result = 0

    # 방문체크 하지 않은 정점에 관해 dfs 탐색
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            result += 1
            dfs(i)
    print("#{} {}".format(tc + 1, result))
