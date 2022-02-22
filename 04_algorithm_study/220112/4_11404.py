# 플로이드

N = int(input())
M = int(input())

distance = [[987654321] * N for _ in range(N)]
for i in range(N):
    distance[i][i] = 0

for _ in range(M):
    st, ed, cost = map(int, input().split())
    distance[st - 1][ed - 1] = min(distance[st - 1][ed - 1], cost)

for k in range(N):
    for i in range(N):
        for j in range(N):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for i in range(N):
    for j in range(N):
        if distance[i][j] == 987654321:
            distance[i][j] = 0
        print(distance[i][j], end=' ')
    print()
