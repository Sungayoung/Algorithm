# def change_num(_num, _k):
#     _num_str = ""
#     while _num > 0:
#         _num_str = str(_num % _k) + _num_str
#         _num //= _k
# _num_str
#
# def eratosthenes(_max_num):
#     is_prime = [True] * (_max_num + 1)
#     is_prime[0] = is_prime[1] = False
#     for i in range(2, _max_num + 1):
#         if is_prime[i]:
#             for j in range(i*2, _max_num+1, i):
#                 is_prime[j] = False
#     return is_prime
#
# def solution(n, k):
#     answer = 0
#     new_num = change_num(n, k)
#     print(new_num)
#     tmp = new_num.split('0')
#     num_list = []
#     for i in range(len(tmp)):
#         if tmp[i]:
#             num_list.append(int(tmp[i]))
#     is_prime = eratosthenes(max(num_list))
#     for num in num_list:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#     else:
#         answer += 1
#
#     return answer
#
# print(solution(1000000, 4))

#     return

def change_num(_num, _k):
    _num_str = ""
    while _num > 0:
        _num_str = str(_num % _k) + _num_str
        _num //= _k

    return _num_str

def solution(n, k):
    answer = 0
    new_num = change_num(n, k)
    tmp = new_num.split('0')
    num_list = []
    for i in range(len(tmp)):
        if tmp[i]:
            num_list.append(int(tmp[i]))
    for num in num_list:
        if num >= 2:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                answer += 1

    return answer

print(solution(437674, 3))