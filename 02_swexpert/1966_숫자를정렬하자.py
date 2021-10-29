# 숫자를 정렬하자

T = int(input())

for tc in range(T):
    num_len = int(input())
    num_list = list(map(int, input().split()))

    for i in range(num_len - 1):
        min_idx = i
        for j in range(i+1, num_len):
            if num_list[j] < num_list[min_idx]:
                min_idx = j
        num_list[min_idx], num_list[i] = num_list[i], num_list[min_idx]

    print("#{} ".format(tc + 1), end="")
    print(*num_list)

