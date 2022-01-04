# AC
from collections import deque

for _ in range(int(input())):
    flag = False
    is_reversed = False
    command = input()
    N = int(input())
    arr = input()
    if len(arr) >= 3:
        q = deque(list(map(int, arr[1:len(arr)-1].split(','))))
    else:
        q = deque()

    for c in command:
        if c == 'R':
            is_reversed = not is_reversed
        elif c == 'D':
            if len(q) == 0:
                flag = True
                break
            if is_reversed:
                q.pop()
            else:
                q.popleft()
    if flag:
        print('error')
    else:
        if is_reversed:
            q.reverse()
        print('[', end="")
        print(*q, sep=',', end="")
        print(']')


