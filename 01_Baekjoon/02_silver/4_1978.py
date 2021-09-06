N = int(input())
num_list = list(map(int, input().split()))
result = []
for num in num_list:
    if num < 2:
        continue
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            break
    else:
        result.append(num)
print(len(result))