# 피보나치 함수
import pprint
for tc in range(int(input())):
    max_len = int(input())
    fibo = [0, 1] + [0] * (max_len - 1)
    idx = 2
    fibo_cnt = [[1, 0], [0, 1]]
    for idx in range(2, max_len + 1):
        fibo[idx] = fibo[idx-1] + fibo[idx - 2]
        fibo_cnt.append([fibo_cnt[idx-1][0] + fibo_cnt[idx-2][0], fibo_cnt[idx-1][1] + fibo_cnt[idx-2][1]])

    print(*fibo_cnt[max_len])
