# 언더프라임

# import time

# start = time.time()

def eratosthenes():
    _is_prime = [True] * 100001
    _is_prime[0] = False
    _is_prime[1] = False
    for _idx in range(2, 100001):
        if not _is_prime[_idx]:
            continue
        for _i in range(_idx * 2, 100001, _idx):
            _is_prime[_i] = False
    return _is_prime


def prime_factor(max_num):
    _prime_factor = [1] * (max_num + 1)
    for _num in range(max_num + 1):
        if is_prime[_num]:
            continue
        for _i in range(2, _num + 1):
            if _num % _i == 0:
                _prime_factor[_num] = _prime_factor[_num // _i] + 1
                # print(f"{_prime_factor[_num]}:{_num} = {_prime_factor[_num//_i]}:{_num//_i} + 1")
                break
    return _prime_factor


num1, num2 = map(int, input().split())

cnt = 0
is_prime = eratosthenes()
prime_factor_list = prime_factor(num2)
for num in range(num1, num2 + 1):
    if is_prime[prime_factor_list[num]]:
        cnt += 1

print(cnt)
# print(time.time() - start)