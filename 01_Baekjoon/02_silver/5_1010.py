T = int(input())
for _ in range(T):
    left, right = map(int, input().split())
    result = 1
    if left == right:
        print(1)
        continue
    for i in range(left):
        result *= right
        right -= 1
    for i in range(left, 0, -1):
        result //= i
    print(result)