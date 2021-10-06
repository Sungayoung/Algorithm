# 마법의 단어
import sys

input = sys.stdin.readline


def perm(_sel, _words):
    if _sel == N:
        words_list.append(_words)
        return

    for _i in range(N):
        if not selected[_i]:
            selected[_i] = True
            perm(_sel + 1, _words + words[_i])
            selected[_i] = False


N = int(input())
words = [input().strip() for _ in range(N)]
words_list = []
selected = [False] * N
K = int(input())
perm(0, "")
result = 0

for idx in range(len(words_list)):
    part_word = words_list[idx]
    cnt = 0
    part_idx = [0] * len(part_word)
    i = 1
    j = 0
    while i < len(part_word):
        if part_word[i] == part_word[j]:
            j += 1
            part_idx[i] = j
        else:
            while j > 0:
                j = part_idx[j-1]
                if part_word[i] == part_word[j]:
                    j += 1
                    part_idx[i] = j
                    break
        i += 1
    compare_word = words_list[idx] + words_list[idx]

    t_idx = 0
    p_idx = 0
    while t_idx < len(compare_word):
        if p_idx == len(part_word):
            cnt += 1
            if cnt > K:
                break
            p_idx = part_idx[p_idx - 1]

        if compare_word[t_idx] == part_word[p_idx]:
            t_idx += 1
            p_idx += 1
        else:
            if p_idx == 0:
                t_idx += 1
            else:
                p_idx = part_idx[p_idx - 1]
    if cnt == K:
        result += 1
print(result)