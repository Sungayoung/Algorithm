for tc in range(int(input())):
    people_len, second, K = map(int, input().split())
    people = list(map(int, input().split()))
    people.sort()
    total = 0
    prev = 0
    result = "Possible"
    for p in people:
        total += ((p - (prev * second)) // second) * K

        # 직전까지 만든 붕어빵 갯수를 저장
        prev = p // second
        total -= 1
        if total < 0:
            result = "Impossible"
            break

    print("#{} {}".format(tc+1, result))