def solution(id_list, report, k):
    answer = []
    report_cnt = [[0] * len(id_list) for _ in range(len(id_list))]
    name_cnt = [0] * len(id_list)
    idx_dict = {}
    for i in range(len(id_list)):
        idx_dict[id_list[i]] = i

    for i in range(len(report)):
        name = report[i].split()

        if report_cnt[idx_dict[name[0]]][idx_dict[name[1]]] == 0:
            report_cnt[idx_dict[name[0]]][idx_dict[name[1]]] = 1
            name_cnt[idx_dict[name[1]]] += 1
    for i in range(len(id_list)):
        cnt = 0
        for j in range(len(id_list)):
            if name_cnt[j] >= k and report_cnt[i][j]:
                cnt += 1
        answer.append(cnt)
    return answer

print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))