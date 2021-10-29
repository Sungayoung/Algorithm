for tc in range(int(input())):
    N = int(input())
    tree = [0] * (N + 1)
    num_list = list(map(int, input().split()))
    last = 1
    for num in num_list:
        tree[last] = num
        cur_idx = last
        while True:
            if cur_idx <= 1:
                break

            # 만약 부모노드보다 자식노드가 더 작다면
            if tree[cur_idx] < tree[cur_idx // 2]:
                tree[cur_idx], tree[cur_idx // 2] = tree[cur_idx // 2], tree[cur_idx]
                cur_idx //= 2
            else:
                break
        last += 1
    result = 0

    while True:
        N //= 2
        if N <= 0:
            break
        result += tree[N]

    print("#{} {}".format(tc+1, result))
