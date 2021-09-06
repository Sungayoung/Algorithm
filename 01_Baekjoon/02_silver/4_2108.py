import time
start = time.time()

# 통계학
import sys

N = int(sys.stdin.readline())

num_list = [int(sys.stdin.readline()) for _ in range(N)]
num_list_len = len(num_list)
num_list.sort()
min_num = num_list[0]
max_num = num_list[-1]
num_cnt = [0] * (max_num - min_num + 1)
num_sum = 0

max_cnt = 0

for num in num_list:
    num_sum += num
    num_cnt[num - min_num] += 1
    if num_cnt[num - min_num] > max_cnt:
        max_cnt = num_cnt[num - min_num]

temp_cnt = 0
result = 0
for idx in range(len(num_cnt)):
    if num_cnt[idx] == max_cnt:
        temp_cnt += 1
        result = idx
    if temp_cnt == 2:
        break

print(round(num_sum / num_list_len))
print(num_list[num_list_len // 2])
print(result + min_num)
print(max_num - min_num)