# 종이 자르기

width, height = map(int, input().split())

N = int(input())

# 첫줄과 끝줄을 넣어줌
width_list = [0, width]
height_list = [0, height]
for _ in range(N):
    tmp = list(map(int, input().split()))
    if tmp[0]:
        width_list.append(tmp[1])
    else:
        height_list.append(tmp[1])

width_list.sort()
height_list.sort()
max_area = 0
for i in range(len(width_list)-1):
    for j in range(len(height_list)-1):
        tmp = (width_list[i+1] - width_list[i]) * (height_list[j+1] - height_list[j])
        if tmp > max_area:
            max_area = tmp

print(max_area)