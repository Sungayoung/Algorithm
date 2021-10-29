# 이진수 표현

for tc in range(int(input())):
    N, num = map(int, input().split())

    result = ""
    if num & ((1 << N) - 1) == (1 << N) - 1:
        result = "ON"
    else:
        result = "OFF"

    print("#{} {}".format(tc+1, result))