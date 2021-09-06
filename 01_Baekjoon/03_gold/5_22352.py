def is_vaccine(before, after, N, M):
    queue = []
    # 인접해있는지 검사하기 위한 4가지 방향. 
    dx_dy = [
        [0, 1], # 오른쪽
        [0, -1],# 왼쪽
        [1, 0], # 아래
        [-1, 0] # 위
    ]

    # 모두 같을 경우
    if before == after:
        return 'YES'
    flag = False
    before_value = 0
    after_value = 0
    cur_pos = []
    
    # 처음 값이 다른 경우를 찾아 이전값, 이후값을 저장한다.
    for i in range(N):
        for j in range(M):
            if before[i][j] != after[i][j]:
                flag = True
                before_value = before[i][j]
                after_value = after[i][j]
                cur_pos = [i, j]
                break
        if flag:
            break
    
    # queue에 처음 값을 넣어줌
    queue.append(cur_pos)

    while queue:
        # queue에서 하나씩 뽑아서 인접 값을 탐색하며 값을 변경한다.
        cur_pos = queue.pop(0)
        before[cur_pos[0]][cur_pos[1]] = after_value
        # 4가지 방향으로 탐색
        for xy in dx_dy:
            if 0<=cur_pos[0]+xy[0]<N and 0<=cur_pos[1] + xy[1]<M:
                temp = [cur_pos[0]+xy[0], cur_pos[1]+xy[1]]
            # 만약 인접한 좌표이고, 이전값과 값이 같다면
                if before[temp[0]][temp[1]] == before_value : 
                    queue.append(temp)              # queue에 인접한 좌표값을 넣어준다
    
    if before == after:
        return 'YES'
    else:
        return 'NO'


N, M = tuple(map(int, input().split())) # N : 세로, M : 가로
before = []
after = []

for _ in range(N):
    before.append(list(map(int, input().split())))
for _ in range(N):
    after.append(list(map(int, input().split())))


print(is_vaccine(before, after, N, M))