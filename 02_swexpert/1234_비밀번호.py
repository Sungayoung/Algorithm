for tc in range(10):
    temp = input().split()
    words_len = int(temp[0])
    words = temp[1]

    stack_list = []
    for word in words:
        if stack_list:
            if word == stack_list[-1]:
                stack_list.pop()
                continue
        stack_list.append(word)
    print("#{}".format(tc+1), end=" ")
    print(*stack_list, sep="")