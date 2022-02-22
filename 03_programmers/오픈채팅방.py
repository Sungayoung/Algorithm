
def solution(record):
    nickname = {}
    result = []
    answer = []
    for line in record:
        tmp = line.split()
        if tmp[0] == 'Enter':
            kind, user_id, user_name = tmp
            nickname[user_id] = user_name
            result.append([kind, user_id])
        elif tmp[0] == 'Change':
            kind, user_id, user_name = tmp
            nickname[user_id] = user_name
        else:
            kind, user_id = tmp
            result.append([kind, user_id])
    for kind, user_id in result:
        if kind == 'Enter':
            answer.append(f"{nickname[user_id]}님이 들어왔습니다.")
        else:
            answer.append(f"{nickname[user_id]}님이 나갔습니다.")

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))