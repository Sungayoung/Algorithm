num_list = list(map(str, range(1, int(input()) + 1)))

for num in num_list:
    if "3" in num or "6" in num or "9" in num:
        cnt = 0
        cnt += num.count("3")
        cnt += num.count("6")
        cnt += num.count("9")
        print("-" * cnt, end="")
    else:
        print(num, end="")
    print(" ", end="")