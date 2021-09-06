for tc in range(int(input())):
    num1_len, num2_len = map(int, input().split())

    num1_list = list(map(int, input().split()))
    num2_list = list(map(int, input().split()))

    if num2_len < num1_len:
        num1_list, num2_list = num2_list, num1_list
        num1_len, num2_len = num2_len, num1_len
    max_mul = -987654321
    for i in range(num2_len - num1_len + 1):
        tmp = 0
        for j in range(num1_len):
            tmp += num1_list[j] * num2_list[i+j]
        if tmp > max_mul:
            max_mul = tmp
    print("#{} {}".format(tc+1, max_mul))