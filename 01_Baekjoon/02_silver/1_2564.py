# 경비원
# 1: 북, 2: 남, 3: 서, 4: 동
width, height = map(int, input().split())
periphery = (width + height) * 2
stores = [tuple(map(int, input().split())) for _ in range(int(input()))]
my_pos = tuple(map(int, input().split()))

# 막무가내로 동서남북 나눠서 풀기
total_dis = 0

for store in stores:
    if my_pos[0] == 1:
        if store[0] == 1:
            total_dis += abs(my_pos[1] - store[1])
        elif store[0] == 2:
            tmp = my_pos[1] + store[1] + height
            total_dis += min(tmp, periphery-tmp)
        elif store[0] == 3:
            total_dis += my_pos[1] + store[1]
        elif store[0] == 4:
            total_dis += (width - my_pos[1]) + store[1]
    elif my_pos[0] == 2:
        if store[0] == 1:
            tmp = my_pos[1] + store[1] + height
            total_dis += min(tmp, periphery - tmp)
        elif store[0] == 2:
            total_dis += abs(my_pos[1] - store[1])
        elif store[0] == 3:
            total_dis += my_pos[1] + (height - store[1])
        elif store[0] == 4:
            total_dis += (width - my_pos[1]) + (height - store[1])
    elif my_pos[0] == 3:
        if store[0] == 1:
            total_dis += my_pos[1] + store[1]
        elif store[0] == 2:
            total_dis += (height - my_pos[1]) + store[1]
        elif store[0] == 3:
            total_dis += abs(my_pos[1] - store[1])
        elif store[0] == 4:
            tmp = my_pos[1] + store[1] + width
            total_dis += min(tmp, periphery - tmp)
    elif my_pos[0] == 4:
        if store[0] == 1:
            total_dis += my_pos[1] + (width - store[1])
        elif store[0] == 2:
            total_dis += (height - my_pos[1]) + (width - store[1])
        elif store[0] == 3:
            tmp = my_pos[1] + store[1] + width
            total_dis += min(tmp, periphery - tmp)
        elif store[0] == 4:
            total_dis += abs(my_pos[1] - store[1])
print(total_dis)
