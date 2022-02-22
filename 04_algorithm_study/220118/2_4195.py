# 친구네트워크
import sys

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)


def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        network[y_root][0] = x_root
        network[x_root][1] += network[y_root][1]
    return network[x_root][1]


def find(x):
    if network[x][0] != x:
        network[x][0] = find(network[x][0])
    return network[x][0]


for tc in range(int(input())):
    network = {}
    for _ in range(int(input())):
        name1, name2 = input().split()
        if not network.get(name1):
            network[name1] = [name1, 1]
        if not network.get(name2):
            network[name2] = [name2, 1]
        # print(name1, name2)
        print(union(name1, name2))
        # print(network)
