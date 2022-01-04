# 팩토리얼 0의 개수

N = int(input())
num = 1
for i in range(2, N + 1):
    num *= i

num = str(num)
count = 0
for i in range(len(num)-1, -1, -1):
    if num[i] == '0':
        count += 1
    else:
        break

print(count)
