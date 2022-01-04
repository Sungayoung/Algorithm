# 덱
from collections import deque
import sys

input = sys.stdin.readline
q = deque()
for _ in range(int(input())):
    command = input().split()
    if command[0] == 'push_front':
        q.appendleft(command[1])
    elif command[0] == 'push_back':
        q.append(command[1])
    elif command[0] == 'pop_front':
        print(q.popleft() if len(q) else -1)
    elif command[0] == 'pop_back':
        print(q.pop() if len(q) else -1)
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        print(0 if len(q) else 1)
    elif command[0] == 'front':
        print(q[0] if len(q) else -1)
    elif command[0] == 'back':
        print(q[-1] if len(q) else -1)
