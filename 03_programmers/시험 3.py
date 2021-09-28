def calculate_time(_time):
    hour, minute = _time.split(':')
    return int(hour) * 60 + int(minute)

def solution(fees, records):
    cur_car = []
    answer = []
    answer_dict = {}
    for i in range(len(records)):
        car_info = records[i].split()
        if car_info[2] == "IN":
            cur_car.append((calculate_time(car_info[0]), car_info[1]))

        elif car_info[2] == "OUT":
            tmp_idx = 0
            for idx in range(len(cur_car)):
                if cur_car[idx][1] == car_info[1]:
                    tmp_idx = idx
                    break

            cur_time = calculate_time(car_info[0])
            passed_time = cur_time - cur_car[tmp_idx][0]

            if answer_dict.get(cur_car[tmp_idx][1], 0):
                answer_dict[cur_car[tmp_idx][1]] += passed_time
            else:
                answer_dict[cur_car[tmp_idx][1]] = passed_time
            cur_car.pop(tmp_idx)

    last_time = calculate_time("23:59")

    for i in range(len(cur_car)):
        passed_time = last_time - cur_car[i][0]
        if answer_dict.get(cur_car[i][1], 0):
            answer_dict[cur_car[i][1]] += passed_time
        else:
            answer_dict[cur_car[i][1]] = passed_time

    tmp_list = sorted(answer_dict.items())
    for k, v in tmp_list:
        if v <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + ((v-fees[0]) // fees[2] if (v-fees[0]) % fees[2] == 0 else (v-fees[0]) // fees[2] + 1) * fees[3])

    return answer

print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))