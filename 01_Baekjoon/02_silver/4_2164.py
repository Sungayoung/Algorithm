# 카드 2

from collections import deque

queue = deque(list(range(1, int(input()) + 1)))

while len(queue) > 1:
    queue.popleft()  # 제일 위에 있는 카드를 바닥에 버리고
    temp = queue.popleft()  # 제일 위에 있는 카드를 제일 아래에 있는 카드밑으로 옮긴다
    queue.append(temp)

print(queue.popleft())
