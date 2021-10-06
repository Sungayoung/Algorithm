import sys
input = sys.stdin.readline
# 컨베이어 벨트 위의 로봇

N, K = map(int, input().split())

# 1은 올리는 위치, N은 내리는 위치
strength = list(map(int, input().split()))
visited = [False] * 2 * N
belt = [0] * 2 * N
cnt = 0
result = 0
start_idx = 0
while True:
    result += 1
    # 1단계
    belt = belt[2*N-1:2*N] + belt[:2*N-1]
    strength = strength[2*N-1:2*N] + strength[:2*N-1]
    if belt[N-1]:       # 내릴 위치의 로봇을 내림
        belt[N-1] = 0

    # 2단계
    tmp = belt[:]
    for i in range(len(belt)-1, 0, -1):
        next_idx = (i + 1) % len(belt)
        if belt[i] and not belt[next_idx] and strength[next_idx] >= 1:
            belt[next_idx] = tmp[i]
            belt[i] = 0
            strength[next_idx] -= 1
            if strength[next_idx] <= 0:
                cnt += 1
                visited[next_idx] = True
        if belt[N - 1]:  # 내릴 위치의 로봇을 내림
            belt[N - 1] = 0

    # 3단계
    if strength[0] > 0:
        belt[0] = 1
        strength[0] -= 1
        if strength[0] <= 0:
            cnt += 1

    # 4단계
    if cnt >= K:
        break

print(result)