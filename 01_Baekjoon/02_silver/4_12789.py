def DFS():
    idx = 0
    order = 1
    stack = []

    while order < N + 1 and idx < N:
        if num_list[idx] == order:
            order += 1
            idx += 1
        else:
            if stack and stack[-1] == order:
                stack.pop()
                order += 1
            else:
                stack.append(num_list[idx])
                idx += 1

    # 스택에 남은 값을 탐색
    while stack:
        if order == stack[-1]:
            stack.pop()
            order += 1
        else:
            return "Sad"

    return "Nice"


N = int(input())
num_list = list(map(int, input().split()))
print(DFS())