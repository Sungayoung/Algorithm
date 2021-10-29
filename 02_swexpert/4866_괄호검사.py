def check_parentness(_word):
    if _word == "(":
        return ")"
    elif _word == "{":
        return "}"


T = int(input())

for tc in range(T):
    words_list = input()
    Stack_list = []

    result = 1
    # 비교를 쉽게 하기위해 괄호만 따로 리스트에 저장

    for idx in range(len(words_list)):
        if words_list[idx] == "(" or words_list[idx] == "{":
            Stack_list.append(words_list[idx])
        elif words_list[idx] == ")" or words_list[idx] == "}":
            if Stack_list:
                if words_list[idx] == check_parentness(Stack_list[-1]):
                    Stack_list.pop()
                # 포함관계가 위배될 때
                else:
                    result = 0
                    break
            # 스택이 비어있는데 닫는 괄호가 입력되었을 때
            else:
                result = 0
                break

    if Stack_list:
        result = 0
    print("#{} {}".format(tc + 1, result))
