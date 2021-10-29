T = int(input())

for tc in range(T):
    total_str, part_str = input().split()

    result = len(total_str)

    if total_str == part_str:
        result = 1
    idx = 0
    while idx < len(total_str) - len(part_str) + 1:
        # 만약 같다면
        if total_str[idx:idx+len(part_str)] == part_str:
            result -= (len(part_str) - 1)
            idx += len(part_str)
        # 아니라면
        else:
            idx += 1
    print("#{} {}".format(tc+1, result))
