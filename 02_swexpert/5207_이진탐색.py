# 이진탐색

for tc in range(int(input())):
    N, M = map(int, input().split())
    num_list = sorted(list(map(int, input().split())))
    find_list = list(map(int, input().split()))
    result = 0
    for find in find_list:
        left = 0
        right = N - 1
        mid = (left + right) // 2
        flag = False
        # 양쪽을 번갈아가며 탐색하는지 판단
        left_flag = False
        right_flag = False
        while left <= right and not flag:

            if num_list[mid] == find:
                result += 1
                flag = True
            # 찾는수가 더 크다면 오른쪽 범위 탐색
            elif num_list[mid] < find:
                if right_flag:
                    break
                right_flag = True
                left_flag = False
                left = mid + 1
                mid = (left + right) // 2
            # 찾는 수가 더 작다면 왼쪽 범위 탐색
            else:
                if left_flag:
                    break
                left_flag = True
                right_flag = False
                right = mid - 1
                mid = (left + right) // 2

    print("#{} {}".format(tc + 1, result))
