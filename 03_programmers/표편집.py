# n: 테이블 갯수, k: 처음 선택된 행의 위치, cmd 수행한 명령어들


def solution(n, k, cmd):
    table = ['O'] * n
    cur = k
    cur_deleted = []
    prev = [0] * n
    next = [0] * n
    prev[0] = -1
    next[n-1] = -1
    for i in range(1, n):
        prev[i] = i - 1
    for i in range(n - 1):
        next[i] = i + 1

    for c in cmd:
        line = c.split()
        if line[0] == "D":
            for _ in range(int(line[1])):
                if next[cur] == -1:
                    break
                cur = next[cur]

        elif line[0] == "U":
            for _ in range(int(line[1])):
                cur = prev[cur]

        elif line[0] == "C":
            table[cur] = "X"
            cur_deleted.append((prev[cur], next[cur], cur))

            if next[cur] == -1:
                next[prev[cur]] = next[cur]
            elif prev[cur] == -1:
                prev[next[cur]] = prev[cur]
            else:
                next[prev[cur]] = next[cur]
                prev[next[cur]] = prev[cur]

            if next[cur] == -1:
                cur = prev[cur]
            else:
                cur = next[cur]
        elif line[0] == "Z":
            tmp_prev, tmp_next, tmp = cur_deleted.pop()

            table[tmp] = "O"
            if prev[tmp] == -1:
                prev[tmp_next] = tmp
            elif tmp_next == -1:
                next[tmp_prev] = tmp
            else:
                next[tmp_prev] = tmp
                prev[tmp_next] = tmp

    answer = "".join(table)
    return answer


solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"])
