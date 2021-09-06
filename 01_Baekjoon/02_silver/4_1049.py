N, M = tuple(map(int, input().split()))

p_price = []
s_price = []
for i in range(M):
    temp = input()
    p_price.append(int(temp.split()[0]))
    s_price.append(int(temp.split()[1]))

min_price = 987654321
min_p_price = min(p_price)
min_s_price = min(s_price)

# 전부 개별로 사는경우 ~ 전부 패키지로 사는 경우 
for i in range(0, N // 6 + 2):
    # print(i * 6)
    cur_price = 0
    cur_price += i * min_p_price
    # print(f'package = {i} * {min_p_price}')
    cur_price += (0 if N - i * 6 < 0 else N - i * 6) * min_s_price
    # print(f'single = {0 if N - i * 6 < 0 else N - i * 6} * {min_s_price}')
    if min_price > cur_price:
        min_price = cur_price
print(min_price)