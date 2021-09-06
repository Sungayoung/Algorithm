# 1 ~ 45까지,
start, end = tuple(map(int, input().split()))

num_list = []
temp = 0
start_idx = 0
end_idx = 0
for i in range(0, 46):
    if temp < start <= temp+i:
        start_idx = i
    if temp < end <= temp+i:
        end_idx = i
    temp += i
    num_list.append(temp)

# print(num_list)
result = 0
# 일단 시작값, 끝값에 해당하는 값의 제곱을 곱해줌
for i in range(start_idx, end_idx + 1):
    result += i ** 2

# 1 2 (2 3 3 3 4 4) 4 4 5 5 5 5 5
# 시작부분에 남는 값, 끝부분에 남는 값을 빼줌
result -= (start - num_list[start_idx-1] - 1) * start_idx
result -= (num_list[end_idx] - end) * end_idx

print(result)