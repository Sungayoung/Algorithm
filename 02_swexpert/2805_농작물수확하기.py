for tc in range(int(input())):
    size = int(input())
    farm = [list(map(int, input().strip())) for _ in range(size)]
    price = 0
    for i in range(size // 2 + 1):
        for j in range(size // 2 - i, size // 2 + i + 1):
            print(i, j)
            price += farm[i][j]
    for i in range(size // 2 + 1, size):
        for j in range(size // 2 - (size - i - 1), size // 2 + (size - i)):
            print(i, j)
            price += farm[i][j]
    print("#{} {}".format(tc + 1, price))
