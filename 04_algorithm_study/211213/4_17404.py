# RGB 거리 2

N = int(input())

# r: 0, g: 1, b: 2

RGB = []
for _ in range(N):
    RGB.append(list(map(int, input().split())))

ans = 987654321

# 마지막꺼랑 첫번째꺼랑 같을 수 없음
for i in range(3):
    dp = [[1000] * N for _ in range(3)]
    dp[i][0] = RGB[0][i]

    for j in range(1, N):
        dp[0][j] = RGB[j][0] + min(dp[1][j-1], dp[2][j-1])
        dp[1][j] = RGB[j][1] + min(dp[0][j-1], dp[2][j-1])
        dp[2][j] = RGB[j][2] + min(dp[0][j-1], dp[1][j-1])

    for j in range(3):
        if i != j:
            ans = min(ans, dp[j][N-1])
print(ans)

