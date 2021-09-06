light_num, length = tuple(map(int, input().split()))

lights = []
# 0: 신호등 위치, 1: 빨간색이 지속되는 시간, 2: 초록색이 지속되는 시간
for _ in range(light_num):
    lights.append(list(map(int, input().split())))

time = 0
prev_pos = 0
for light in lights:
    time += light[0] - prev_pos
    prev_pos = light[0]
    # 지금 빨간불일 때
    if time % (light[1] + light[2]) <= light[1]:    # 왜 <= 부등호 써야하쥬..? <이거 썼더니 계속 틀려서
        # print(f'{time} += {light[1] - (time % (light[1] + light[2]))}')
        time += light[1] - (time % (light[1] + light[2]))
    # print(time)


time += length - prev_pos

print(time)