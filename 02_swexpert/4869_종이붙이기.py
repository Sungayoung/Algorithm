T = int(input())

for tc in range(T):
    num = int(input()) // 10
    memo = [0, 1, 3]

    for i in range(3, num+1):

        # 이유는 모르겠지만 아래와 같은 규칙이 보임
        if num % 2 == 0:
            memo.append(memo[i - 2] * 4 - 1)
        else:
            memo.append(memo[i - 2] * 4 + 1)
    print("#{} {}".format(tc+1, memo[num]))
