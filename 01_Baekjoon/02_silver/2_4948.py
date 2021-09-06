# 베르트랑 공준

N = 246912  # 최대 n이 123456이라 했으므로
is_prime = [1] * (N + 1)


# 에라토스테네스의 채
for i in range(2, N + 1):
    if is_prime[i] == 1:
        for idx in range(i * 2, N + 1, i):
            is_prime[idx] = 0

while True:
    num = int(input())
    if num == 0:
        break
    print(sum(is_prime[num+1:num * 2 + 1]))
