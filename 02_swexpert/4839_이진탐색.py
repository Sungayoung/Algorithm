T = int(input())

for tc in range(T):
    page_len, A_page, B_page = map(int, input().split())

    page = list(range(1, page_len + 1))
    start = 0
    end = page_len - 1
    A_cnt = 0
    B_cnt = 0
    result = ""

    # A 횟수
    while start <= end:
        mid = (start + end) // 2
        A_cnt += 1
        if page[mid] == A_page:
            break
        # 중간페이지를 기준으로 하므로 mid + 1이 아닌 mid로 다시 설정
        elif page[mid] < A_page:
            start = mid
        else:
            end = mid

    # 인덱스 리셋
    start = 0
    end = page_len - 1

    # B 횟수
    while start <= end:
        mid = (start + end) // 2
        B_cnt += 1
        if page[mid] == B_page:
            break
        elif page[mid] < B_page:
            start = mid
        else:
            end = mid

    if A_cnt > B_cnt:
        result = "B"
    elif A_cnt < B_cnt:
        result = "A"
    else:
        result = "0"

    print("#{} {}".format(tc + 1, result))
