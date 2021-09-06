def str_mapping(_str):
    if _str in "CEFGHIJKLMNSTUVWXYZ":
        return 0
    elif _str in "ADOPQR":
        return 1
    elif _str == "B":
        return 2


for tc in range(int(input())):
    str1, str2 = input().split()
    result = "SAME"
    if len(str1) != len(str2):
        result = "DIFF"
    else:
        for idx in range(len(str1)):
            if str_mapping(str1[idx]) != str_mapping(str2[idx]):
                result = "DIFF"
                break

    print("#{} {}".format(tc + 1, result))
