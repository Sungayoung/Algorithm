T = int(input())

for tc in range(T):
    words = list(input())

    flag = True
    while flag:

        # 초기값 False로 세팅, 만약 같은문자가 하나라도 없으면 반복문 종료
        flag = False
        idx = 0
        while idx < len(words) - 1:
            if words[idx] == words[idx+1]:

                # 이미 idx번째 문자를 pop해서 한칸씩 당겨졌으므로
                words.pop(idx)
                words.pop(idx)

                flag = True     # 같은 문자열이 있다면 계속 반복
            else:
                idx += 1
    print("#{} {}".format(tc+1, len(words)))

