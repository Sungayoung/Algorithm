import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    result = ""
    str_list = [list(input()) for _ in range(N)]
    flag = False
    # 가로의 경우
    for i in range(N):
        for j in range(N - M + 1):
            for l in range(M // 2):
                if str_list[i][j+l] != str_list[i][j+(M-l)-1]:
                    break

            else:
                result = "".join(str_list[i][j:j+M])
                flag = True
                break   # 회문은 하나밖에 없다고 했으므로
        if flag:
            break

    flag = False
    # 세로의 경우
    for i in range(N):
        for j in range(N - M + 1):
            for l in range(M // 2):
                if str_list[j+l][i] != str_list[j+(M-l)-1][i]:
                    break
            else:
                result = "".join([row[i] for row in str_list[j:j+M]])
                flag = True
                break   # 회문은 하나밖에 없다고 했으므로
        if flag:
            break

    print("#{} {}".format(tc+1, result))