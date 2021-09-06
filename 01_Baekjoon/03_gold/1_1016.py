def eratosthenes(_min, _max):
    _len = _max - _min + 1
    _is_divided = [1] * _len
    _max_idx = int(_max ** 0.5)
    # 최소 제곱수 4부터 탐색
    for _idx in range(2, _max_idx + 1):
        _num = _idx ** 2
        _start = 0

        # 시작점을 지정해줌
        if _min % _num == 0:
            _start = _min
        else:
            _start = (_min // _num + 1) * _num

        # 시작점이 범위내에 있고 만약 이미 지웠다면
        if _min <= _start <= _max:
            for i in range(_start, _max+1, _num):
                _is_divided[i-_min] = 0

    return sum(_is_divided)


min_num, max_num = map(int, input().split())
print(eratosthenes(min_num, max_num))