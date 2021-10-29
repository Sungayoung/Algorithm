# 퀵정렬


def hoare_partition(left, right):
    global num_list
    pivot = num_list[left]
    l = left + 1
    r = right

    while l <= r:
        while l <= r and num_list[l] <= pivot:
            l += 1
        while l <= r and num_list[r] >= pivot:
            r -= 1

        if l <= r:
            num_list[l], num_list[r] = num_list[r], num_list[l]
    num_list[left], num_list[r] = num_list[r], num_list[left]
    return r


def lomuto(left, right):
    global num_list
    i = left - 1
    pivot = num_list[right]
    for j in range(left, right):
        if num_list[j] <= pivot:
            i += 1
            num_list[i], num_list[j] = num_list[j], num_list[i]

    num_list[i + 1], num_list[right] = num_list[right], num_list[i + 1]
    return i + 1


def quick_sort(left, right):
    if left >= right:
        return

    mid = lomuto(left, right)

    quick_sort(left, mid - 1)
    quick_sort(mid + 1, right)


for tc in range(int(input())):
    N = int(input())
    num_list = list(map(int, input().split()))
    quick_sort(0, N - 1)

    print("#{} {}".format(tc + 1, num_list[N // 2]))
