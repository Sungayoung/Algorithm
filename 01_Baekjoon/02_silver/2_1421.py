input_list = list(map(int, input().split()))

N = input_list[0]
C = input_list[1]       # 나무를 자를 때 드는 돈
W = input_list[2]       # 나무의 가격

tree_list = []
for i in range(N):
    tree_list.append(int(input()))

tree_list.sort()
max_price = 0

# K = 0       # 나무의 갯수
# L = 0       # 나무의 길이
for i in range(1, tree_list[-1] + 1):
    price = 0
    for tree in tree_list:
        cost = i * (tree // i) * W - (tree // i if tree % i else tree // i - 1) * C
        if cost > 0:
            price += cost

    if price > max_price:
        max_price = price

if max_price < 0:
    max_price = 0

print(max_price)