P = int(input())

max_strength = 100
minus = list(map(int, input().split()))
plus = list(map(int, input().split()))

# 무게별로 행복의 최대값을 담음.
# 각 인덱스는 체력, 사람의 수 범위 내에서의 행복의 최대값을 가지고있음
dp = [[0] * (max_strength + 1) for _ in range(P + 1)]

for i in range(1, P + 1):
    for j in range(max_strength):   # 체력이 0이 되면 죽은것
        if minus[i-1] <= j:
            # 현재 idx 값을 담지 않는 것, 현재 idx 값을 담는것 둘 중에 큰값
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - minus[i-1]] + plus[i-1])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[P][99])
