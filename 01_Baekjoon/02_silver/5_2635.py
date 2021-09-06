# 수 이어가기

max_num = int(input())
max_cnt = 0
max_list = []
for num in range(max_num, 0, -1):
    cnt = 1
    prev = max_num
    cur = num
    tmp_list = [prev, cur]
    while cur >= 0:
        tmp = cur
        cur = prev - cur
        prev = tmp
        cnt += 1
        tmp_list.append(cur)
    if cnt > max_cnt:
        max_cnt = cnt
        max_list = tmp_list[:cnt]
print(max_cnt)
print(*max_list)
