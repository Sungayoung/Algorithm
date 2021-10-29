# 전자카트
def perm(idx):
    global min_value
    if idx == size:
        tmp_value = 0
        for j in range(size - 1):
            tmp_value += energy[selected[j]][selected[j + 1]]
        tmp_value += energy[selected[-1]][0]
        if tmp_value < min_value:
            min_value = tmp_value
        return

    for i in range(1, size):
        if not visited[i]:
            selected[idx] = i
            visited[i] = True
            perm(idx + 1)
            visited[i] = False


for tc in range(int(input())):
    size = int(input())
    energy = [list(map(int, input().split())) for _ in range(size)]

    # 현재까지 고른 값
    selected = [False] * size
    visited = [False] * size
    selected[0] = 0
    visited[0] = True

    min_value = 987654321
    perm(1)
    print("#{} {}".format(tc+1, min_value))
