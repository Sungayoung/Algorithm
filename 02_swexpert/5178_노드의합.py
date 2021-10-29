for tc in range(int(input())):
    # N: 노드의 개수, M: 리프노드의 개수, L: 값을 출력할 노드 번호
    N, M, L = map(int, input().split())

    tree = [0] * (N + 1)

    for _ in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value

    # 트리의 맨 마지막 인덱스값부터 탐색
    for idx in range(N, 0, -1):
        if idx // 2 <= 0:
            continue
        if tree[idx // 2]:
            continue
        parent = idx // 2
        left = parent * 2
        right = parent * 2 + 1
        if left <= N and right <= N:
            tree[parent] = tree[left] + tree[right]
        elif left <= N:
            tree[parent] = tree[left]
    print("#{} {}".format(tc+1, tree[L]))