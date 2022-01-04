# 앱

N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
cost_sum = sum(cost)
dp = [[0] * (cost_sum + 1) for _ in range(N)]

for c in range(cost_sum + 1):
    if cost[0] <= c:
        dp[0][c] = memory[0]

for i in range(1, N):
    for c in range(cost_sum + 1):
        if cost[i] <= c:
            dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - cost[i]] + memory[i])
        else:
            dp[i][c] = dp[i - 1][c]

result = 0
for c in range(cost_sum + 1):
    if dp[N-1][c] >= M:
        result = c
        break

print(result)

