T = int(input())

for i in range(T):

    # 각 테스트 케이스의 값을 입력받음
    trash_input = []
    weight_limit, n = tuple(map(int, input().split()))
    for j in range(n):
        #  list input 0 : 거리, 1 : 무게
        trash_input.append(list(map(int, input().split())))
    
    # print(trash_input)
    total_distance = 0
    cur_weight = 0
    cur_position = 0
   
    while cur_position < n:
        # print(cur_position)
        # 만약 쓰레기차가 공간이 남았다면
        if trash_input[cur_position][1] + cur_weight < weight_limit:
            cur_weight += trash_input[cur_position][1]
            cur_position += 1
        
        # 쓰레기차 공간이 딱 맞게 찼다면
        elif trash_input[cur_position][1] + cur_weight == weight_limit:
            total_distance += trash_input[cur_position][0] * 2
            cur_weight = 0
            cur_position += 1
        
        # 쓰레기차 공간이 모자른다면
        else:
            total_distance += trash_input[cur_position][0] * 2
            cur_weight = 0
    
    # 만약 쓰레기차에 아직 쓰레기가 남아있다면
    if cur_weight:
        total_distance += trash_input[-1][0] * 2
    
    print(total_distance)
    
