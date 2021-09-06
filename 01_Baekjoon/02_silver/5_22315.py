def math_is_physical(num_string):
    result = ''

    # 시작 숫자가 한자리수인 경우
    start = int(num_string[0])-1
    while len(result) < len(num_string):
        if result in num_string:
            start += 1
            result += str(start)
            # print(result, start)
        else:
            break
    # print(f"result : {result}, num_string : {num_string}")
    if result == num_string:
        return(int(num_string[0]), start)

    result = ''
    # 시작 숫자가 두자리수인 경우
    start = int(num_string[0:2])-1
    while len(result) < len(num_string):
        if result in num_string:
            start += 1
            result += str(start)
            # print(result, start)
        else:
            break
    # print(f"result : {result}, num_string : {num_string}")
    if result == num_string:
        return(int(num_string[0:2]), start)

    result = ''
    # 시작 숫자가 세자리수인 경우
    start = int(num_string[0:3])-1
    while len(result) < len(num_string):
        if result in num_string:
            start += 1
            result += str(start)
            # print(result, start)
        else:
            break
    # print(f"result : {result}, num_string : {num_string}")
    if result == num_string:
        return(int(num_string[0:3]), start)


num_string = input()

print(*math_is_physical(num_string), sep=" ")