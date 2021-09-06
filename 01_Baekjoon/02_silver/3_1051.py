def max_square_size(square, max_x, max_y):
    if len(square) == 1:
        return 1
    min_len = min(max_x, max_y)
    for size in range(min_len, 1, -1):
        # print(size)
        for y in range(0, max_y - size + 1):
            for x in range(0, max_x - size + 1):
                # print(y, x)
                if square[y][x] == square[y+size-1][x] == square[y][x+size-1] == square[y+size-1][x+size-1]:
                    # print(f"{square[y][x]}({y, x}) == {square[y+size-1][x]}({y+size-1, x}) == {square[y][x+size-1]}({y, x+size-1}) == {square[y+size-1][x+size-1]}({y+size-1, x+size-1})")
                    return size ** 2
    else:
        return 1


max_y, max_x = tuple(map(int, input().split()))

square = []
for y in range(max_y):
    square.append(list(map(int, list(input()))))

print(max_square_size(square, max_x, max_y))

