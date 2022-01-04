# 평범한 배낭

N, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N)]
weight, value = map(int, input().split())
for j in range(K + 1):
    if j >= weight:
        dp[0][j] = value

for i in range(1, N):
    weight, value = map(int, input().split())
    for j in range(K + 1):
        if j >= weight:
            dp[i][j] = max(dp[i - 1][j], value + dp[i - 1][j - weight])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])