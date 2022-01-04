# 탈옥

for tc in range(int(input())):
    height, width = map(int, input().split())
    prisoner = []
    board = []
    for i in range(height):
        tmp = list(input())
        for j in range(width):
            if tmp[j] == '$':
                prisoner.append((i, j))


