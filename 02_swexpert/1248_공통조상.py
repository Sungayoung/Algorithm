# 공통조상

for tc in range(int(input())):
    V, E, v1, v2 = map(int, input().split())

    parents = [0] * (V + 1)
    child = [0] * (V + 1)
    tree_info = list(map(int, input().split()))
    for i in range(E):
        parents[tree_info[i * 2 + 1]] = tree_info[i * 2]

    # 본인 포함 서브트리 노드의 수를 저장
    for i in range(1, V + 1):
        tmp = i
        while tmp >= 1:
            child[tmp] += 1
            tmp = parents[tmp]

    v1_parents = set()
    while v1 >= 1:
        v1_parents.add(parents[v1])
        v1 = parents[v1]

    result = 0
    while v2 >= 1:
        if v2 in v1_parents:
            result = v2
            break
        v2 = parents[v2]

    print("#{} {} {}".format(tc + 1, result, child[result]))
