# 축사배정

# N: 소의 수, M: 축사의 수
N, M = map(int, input().split())

graph = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    num_list = list(map(int, input().split()))
    for j in range(1, len(num_list)):
        graph[i][num_list[j]] = 1

home = [-1] * M
