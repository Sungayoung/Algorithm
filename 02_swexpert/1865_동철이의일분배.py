# 동철이의 일분배
def percent_to_float(num):
    return num / 100


def perm(sel, success):
    global max_success
    if sel == N:
        max_success = max(max_success, success)
        return

    for i in range(N):
        if not visited[i]:
            new_success = success * probability[sel][i]
            visited[i] = True
            if new_success > max_success:
                perm(sel + 1, new_success)
            visited[i] = False


for tc in range(int(input())):
    N = int(input())

    probability = []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        probability.append(list(map(percent_to_float, tmp)))
    max_success = -1
    visited = [False] * N
    perm(0, 1)
    print("#{} {:6f}".format(tc+1, round(max_success * 100, 6)))
