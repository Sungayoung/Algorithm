def cal(_num1, _num2, _word):
    if _word == "+":
        return _num1 + _num2
    elif _word == "-":
        return _num1 - _num2
    elif _word == "*":
        return _num1 * _num2
    elif _word == "/":
        if _num2:
            return _num1 // _num2


def calculator():
    stack = []
    for token in postfix:
        if token == ".":
            break
        elif token.isdigit():
            stack.append(int(token))
        else:
            try:
                num2 = stack.pop()
                num1 = stack.pop()
                result = cal(num1, num2, token)

                # 나누려는 숫자가 0일 경우 error
                if not result:
                    return "error"
                stack.append(result)
            except:
                return "error"
    if len(stack) == 1:
        return stack[0]
    else:
        return "error"


for tc in range(int(input())):
    postfix = input().strip().split()
    print("#{} {}".format(tc + 1, calculator()))
