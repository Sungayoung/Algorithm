def inorder(idx):
    global num
    if idx * 2 <= N:
        inorder(idx * 2)
    tree[idx] = num
    num += 1
    if idx * 2 + 1 <= N:
        inorder(idx * 2 + 1)


for tc in range(int(input())):
    N = int(input())

    tree = [0] * (N + 1)
    num = 1
    inorder(1)
    print("#{} {} {}".format(tc+1, tree[1], tree[N//2]))

