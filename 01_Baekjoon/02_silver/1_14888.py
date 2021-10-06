def calculator(num1, num2, op):
    if op == 0:
        return num1 + num2
    elif op == 1:
        return num1 - num2
    elif op == 2:
        return num1 * num2
    else:
        # c++14 표준
        if num1 < 0:
            _tmp = (num1 * -1) // num2
            return _tmp * -1
        return num1 // num2


# 순열
def perm(idx, num):
    global result

    if idx == N:
        result.append(num)
        return

    for _i in range(N):
        if not sel[_i]:
            sel[_i] = True
            perm(idx + 1, calculator(num, num_list[idx + 1], operator[_i]))
            sel[_i] = False


# 연산자 끼워넣기

num_len = int(input())

num_list = list(map(int, input().split()))

# + - * / (연산자 우선순위 무시)
tmp = list(map(int, input().split()))
N = sum(tmp)
operator = []

# 순열을 쉽게 만들기 위해서 이어진 배열로 만들어줌
for i in range(4):
    operator.extend([i] * tmp[i])
sel = [False] * N
result = []
perm(0, num_list[0])

print(max(result))
print(min(result))