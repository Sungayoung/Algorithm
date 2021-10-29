# 병합정렬
def merge_sort(_num_list):
    if len(_num_list) == 1:
        return _num_list
    mid = len(_num_list) // 2
    left = merge_sort(_num_list[:mid])
    right = merge_sort(_num_list[mid:])
    return merge(left, right)


def merge(left_list, right_list):
    global answer

    # 왼쪽 마지막 원소, 오른쪽 마지막 원소 비교
    # flag = False
    # if left_list[-1] > right_list[-1]:
    #     flag = True

    l, r = 0, 0
    sorted_list = []
    while l < len(left_list) and r < len(right_list):
        if left_list[l] <= right_list[r]:
            sorted_list.append(left_list[l])
            l += 1
        else:
            sorted_list.append(right_list[r])
            r += 1
    if l < len(left_list):
        answer += 1

    while l < len(left_list):
        sorted_list.append(left_list[l])
        l += 1

    while r < len(right_list):
        sorted_list.append(right_list[r])
        r += 1

    # if flag:
    #     answer += 1
    return sorted_list


for tc in range(int(input())):
    N = int(input())
    num_list = list(map(int, input().split()))
    answer = 0

    print("#{} {} {}".format(tc + 1, merge_sort(num_list)[N // 2], answer))
