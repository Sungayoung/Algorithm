# 괄호추가하기

def calc(_num1, _num2, _op):
    if _op == '+':
        return _num1 + _num2
    elif _op == '-':
        return _num1 - _num2
    elif _op == '*':
        return _num1 * _num2


def recursion(num, idx):
    global max_num
    if idx >= num_N:
        if num > max_num:
            max_num = num
        return
    # 다음에 괄호가 있는 경우
    if idx + 1 < num_N:
        recursion(calc(num, calc(nums[idx], nums[idx + 1], op[idx]), op[idx - 1]), idx + 2)
    # 다음에 괄호가 없는 경우
    recursion(calc(num, nums[idx], op[idx - 1]), idx + 1)


N = int(input())
num_N = N // 2 + 1
nums = []
op = []
tmp = input()
for i in range(N):
    if i % 2:
        op.append(tmp[i])
    else:
        nums.append(int(tmp[i]))

max_num = -(2 ** 31)

recursion(nums[0], 1)
print(max_num)
