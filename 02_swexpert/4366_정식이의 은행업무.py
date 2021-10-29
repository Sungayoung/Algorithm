# 정식이의 은행업무
def change_num(num, n):
    answer = 0
    power = 0
    for idx in range(len(num) - 1, -1, -1):
        answer += num[idx] * (n ** power)
        power += 1

    return answer


def find_decimal(bin_num, ter_num):
    # 모든 2진수 자리 탐색
    for i in range(len(bin_num)):
        bin_num[i] = (bin_num[i] + 1) % 2
        new_binary_num = change_num(bin_num, 2)

        # 모든 3진수 자리 탐색
        for j in range(len(ter_num)):
            tmp_ternary = ter_num[:]
            for k in range(2):
                tmp_ternary[j] = (tmp_ternary[j] + 1) % 3
                new_ternary_num = change_num(tmp_ternary, 3)
                if new_ternary_num == new_binary_num:
                    return new_binary_num
        bin_num[i] = (bin_num[i] + 1) % 2


for tc in range(int(input())):
    binary_num = list(map(int, input()))
    ternary_num = list(map(int, input()))
    print("#{} {}".format(tc + 1, find_decimal(binary_num, ternary_num)))
