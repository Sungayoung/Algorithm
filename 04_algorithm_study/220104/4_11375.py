# 열혈강호
import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline


def minus_1(num):
    return int(num) - 1


def dfs(x):
    for v in graph[x]:
        if not visited[v]:
            visited[v] = True
            if connected[v] == -1 or dfs(connected[v]):
                connected[v] = x
                return True
    return False


N, M = map(int, input().split())
graph = [list(map(minus_1, input().split()))[1:] for _ in range(N)]
connected = [-1] * M
ans = 0
for i in range(N):
    visited = [False] * M
    if dfs(i):
        ans += 1

print(ans)
