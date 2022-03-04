def solution(user_id, banned_id):
    candidate_list = []
    for ban in banned_id:
        candidate = []
        for user in user_id:

            if len(ban) == len(user):
                for idx in range(len(user)):
                    if ban[idx] != '*' and ban[idx] != user[idx]:
                        break
                else:
                    candidate.append(user)
        candidate_list.append(candidate)

    answer = []
    selected = []

    def comb(_idx):
        nonlocal answer
        if _idx == len(banned_id):
            sorted_list = sorted(selected)
            if sorted_list not in answer:
                answer.append(sorted_list)
            return

        for _candidate in candidate_list[_idx]:
            if _candidate not in selected:
                selected.append(_candidate)
                comb(_idx + 1)
                selected.pop()
    comb(0)
    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
