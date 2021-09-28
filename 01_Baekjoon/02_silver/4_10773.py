# 제로

stack = []
for _ in range(int(input())):
    num = int(input())
    if num:
        stack.append(num)
    else:
        stack.pop()
print(sum(stack))
