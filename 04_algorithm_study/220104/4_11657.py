# 타임머신

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(M)]
distance = [987654321] * N
distance[0] = 0
ans = 987654321
for i in range(N):
    for j in range(M):
        st = graph[j][0] - 1
        ed = graph[j][1] - 1
        cost = graph[j][2]
        if distance[st] == 987654321:
            continue
        if distance[ed] > distance[st] + cost:
            distance[ed] = distance[st] + cost

for j in range(M):
    st = graph[j][0] - 1
    ed = graph[j][1] - 1
    cost = graph[j][2]

    if distance[st] == 987654321:
        continue
    if distance[ed] > distance[st] + cost:
        ans = -1

if ans == -1:
    print(ans)
else:
    for i in range(1, N):
        if distance[i] == 987654321:
            print(-1)
        else:
            print(distance[i])
