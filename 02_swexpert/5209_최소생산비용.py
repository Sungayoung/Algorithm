# 최소생산비용
def perm(sel, cost):
    global min_cost
    if sel == N:
        min_cost = min(min_cost, cost)
        return

    for i in range(N):
        if not visited[i]:
            new_cost = cost + factory[sel][i]
            visited[i] = True

            # 현재 가지고있는 최소비용보다 작을때만
            if new_cost < min_cost:
                perm(sel + 1, new_cost)
            visited[i] = False


for tc in range(int(input())):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]

    min_cost = 987654321
    visited = [False] * N
    perm(0, 0)
    print("#{} {}".format(tc+1, min_cost))
