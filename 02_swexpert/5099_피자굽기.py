for tc in range(int(input())):
    size, pizza_len = map(int, input().split())
    temp = list(map(int, input().split()))
    pizza = []
    for i in range(pizza_len):
        pizza.append([temp[i], i + 1])
    cnt_zero = 0
    check = [False] * pizza_len
    fire = pizza[0: size]
    pizza_idx = size
    fire_idx = 0
    while True:
        fire[fire_idx][0] //= 2
        if fire[fire_idx][0] <= 0:
            # 한번 0 이하로 떨어진 곳은 체크하지 않음.
            if not check[fire[fire_idx][1] - 1]:
                check[fire[fire_idx][1] - 1] = True

                # 피자가 이미 다 화덕에 들어갔다면 수행하지 않음
                if pizza_idx < pizza_len:
                    # 화덕에서 꺼내고 바로 그자리에 남은 피자를 넣음.
                    fire[fire_idx] = pizza[pizza_idx]
                cnt_zero += 1   # 0의 갯수
                pizza_idx += 1

                # 0의 갯수가 피자길이 - 1이면 즉시 반복문 종료
                if cnt_zero == pizza_len - 1:
                    break
        fire_idx = (fire_idx + 1) % len(fire)
    result = 0

    for i in range(len(fire)):
        if fire[i][0]:
            result = fire[i][1]
            break
    print("#{} {}".format(tc+1, result))