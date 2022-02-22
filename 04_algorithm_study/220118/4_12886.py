# 돌 그룹
from collections import deque

nums = list(map(int, input().split()))
num_sum = sum(nums)
ans = 0
if num_sum % 3:
    ans = 0
else:
    visited = set()
    nums.sort()
    visited.add(tuple(nums))
    q = deque()
    q.append(nums)
    while q:
        a, b, c = q.popleft()
        # print(a, b, c)
        if a == b == c:
            ans = 1
            break

        for (x, y) in [(a, b), (b, c), (c, a)]:
            # print(x, y)
            if x == y:
                continue
            elif x > y:
                x, y = y, x
            y -= x
            x += x
            z = num_sum - x - y
            if x < 0 or y < 0 or z < 0:
                continue
            new_nums = tuple(sorted([x, y, z]))
            if new_nums not in visited:
                visited.add(new_nums)
                q.append(new_nums)
print(ans)
