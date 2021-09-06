import time

start = time.time()


# 신기한 소수
# def eratosthenes(_num):
#     _is_prime = [True] * (10 ** _num)
#     _is_prime[0] = False
#     _is_prime[1] = False
#     len_list = len(_is_prime)
#     for _i in range(2, int(len_list ** 0.5) + 1):
#         if not _is_prime[_i]:
#             continue
#         for _idx in range(_i * _i, len_list, _i):
#             _is_prime[_idx] = False
#     return _is_prime


def strange_prime_num(_num):
    _prime_list = [[2, 3, 5, 7]]
    for _idx in range(_num-1):
        temp_list = []
        for _prime in _prime_list[_idx]:
            for _j in range(1, 10, 2):
                _tmp = _prime * 10 + _j
                for _k in range(3, int(_tmp ** 0.5) + 1):
                    if _tmp % _k == 0:
                        break
                else:
                    temp_list.append(_tmp)
        _prime_list.append(temp_list)
    return _prime_list


length = int(input())
prime_list = strange_prime_num(length)
print(*prime_list[length-1], sep="\n")
