T = int(input())

for tc in range(T):
    part_str = input()      #XYPV
    total_str = input()     #EOGGXYPVSY
    result = 0
    if part_str == total_str:
        result = 1

    for i in range(len(total_str) - len(part_str) + 1):
        for j in range(len(part_str)):
            if total_str[i+j] != part_str[j]:
                break
        else:
            result = 1
    print("#{} {}".format(tc+1, result))
