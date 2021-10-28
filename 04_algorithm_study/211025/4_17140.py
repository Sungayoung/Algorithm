# 이차원 배열과 연산
from copy import deepcopy

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
height = 3
width = 3
time = -1
for time in range(101):
    if 0 <= r - 1 < height and 0 <= c - 1 < width and arr[r - 1][c - 1] == k:
        print(time)
        break
    tmp_height = height
    tmp_width = width
    new_arr = []
    if height >= width:
        for i in range(height):
            num_dict = {}
            for j in range(width):
                if arr[i][j] == 0:
                    continue
                if num_dict.get(arr[i][j]):
                    num_dict[arr[i][j]] += 1
                else:
                    num_dict[arr[i][j]] = 1
            num_list = sorted(num_dict.items(), key=lambda x: (x[1], x[0]))
            tmp_list = []
            for num in num_list:
                tmp_list.extend(num)
            new_arr.append(tmp_list)
            if len(tmp_list) > tmp_width:
                tmp_width = len(tmp_list)

        for i in range(height):
            new_arr[i].extend([0] * (tmp_width - len(new_arr[i])))

        arr = deepcopy(new_arr)

    else:
        for j in range(width):
            num_dict = {}
            for i in range(height):
                if arr[i][j] == 0:
                    continue
                if num_dict.get(arr[i][j]):
                    num_dict[arr[i][j]] += 1
                else:
                    num_dict[arr[i][j]] = 1
            num_list = sorted(num_dict.items(), key=lambda x: (x[1], x[0]))
            tmp_list = []
            for num in num_list:
                tmp_list.extend(num)
            new_arr.append(tmp_list)
            if len(tmp_list) > tmp_height:
                tmp_height = len(tmp_list)

        for i in range(width):
            new_arr[i].extend([0] * (tmp_height - len(new_arr[i])))
        arr = list(map(list, zip(*new_arr)))

    width = min(100, tmp_width)
    height = min(100, tmp_height)
else:
    print(-1)
